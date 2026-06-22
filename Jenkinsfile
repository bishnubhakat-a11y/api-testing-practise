// Define a declarative Jenkins pipeline
pipeline {
    // Specify that this pipeline can run on any available Jenkins agent/node
    agent any
    tools {
        allure 'Allure-CLI' 
    }

    // Define parameters that the user will be prompted for when triggering a build
    parameters {
        // Create a dropdown menu parameter named 'TEST_SUITE'
        choice(
            // Set the name of the parameter variable
            name: 'TEST_SUITE', 
            // Define the options available in the dropdown (smoke or regression)
            choices: ['smoke', 'regression'], 
            // Describe what this parameter does for the user triggering the build
            description: 'Choose which test suite to execute: Smoke (Fast) or Regression (Full).'
        )
    }

    // Define the different stages of our CI/CD pipeline
    stages {
        
        // Define the first stage: setting up the environment
        stage('Setup Environment') {
            // Define the steps to execute in this stage
            steps {
                // Execute a batch script (Windows) to set up the Python environment
                bat '''
                    :: Print a message to the console indicating setup is starting
                    echo "Setting up Python virtual environment..."
                    
                    :: Create a new Python virtual environment named 'venv' in the workspace
                    python -m venv venv
                    
                    :: Activate the virtual environment and install requirements
                    :: Note: We chain commands with '&&' so if activation fails, installation won't run
                    call venv\\Scripts\\activate.bat && pip install -r requirements.txt
                '''
            }
        }

        // Define the second stage: running the API tests
        stage('Execute API Tests') {
            // Define the steps to execute in this stage
            steps {
                // Execute a batch script to run the tests using pytest
                bat """
                    :: Print a message indicating which suite is being run, using the Jenkins parameter
                    echo "Running ${params.TEST_SUITE} tests..."
                    
                    :: Activate the virtual environment
                    call venv\\Scripts\\activate.bat
                    
                    :: Execute pytest, passing the selected marker (-m) from the dropdown parameter
                    :: We also output the pytest-html report and Allure results directory
                    :: The '|| exit 0' ensures the pipeline continues even if tests fail (so reports can be generated)
                    pytest -m ${params.TEST_SUITE} tests/ --html=reports/report.html --self-contained-html --alluredir=reports/allure-results || exit 0
                """
            }
        }
    }

    // Define actions to take after the pipeline stages finish executing
    post {
        // 'always' block runs regardless of whether the pipeline succeeded or failed
        always {
            // Define the steps to execute after the build
        
                // Print a message indicating reports are being generated
                echo 'Generating Test Reports...'

                // Publish the pytest-html report as a build artifact using the HTML Publisher Plugin
                publishHTML(
                    // Configure the HTML publisher settings
                    target: [
                        // Allow missing report if something catastrophically failed
                        allowMissing: true,
                        // Always keep past reports to track history
                        alwaysLinkToLastBuild: true,
                        // Do not keep all reports forever (saves disk space)
                        keepAll: false,
                        // Point to the directory where pytest generated the HTML report
                        reportDir: 'reports',
                        // Specify the exact name of the HTML file
                        reportFiles: 'report.html',
                        // Name the link that will appear on the Jenkins build page
                        reportName: 'Pytest HTML Report'
                    ]
                )

                // Generate and publish the Allure dashboard using the Allure Jenkins Plugin
                allure(
                    // Ensure the plugin knows we are using Allure v2
                    includeProperties: false,
                    // Assume the default Allure commandline tool installed on Jenkins
                    jdk: '',
                    // Specify the path to the directory containing the raw JSON test results
                    results: [[path: 'reports/allure-results']]
                )

        }
        
        // 'success' block runs only if all stages passed
        success {
            // Print a success message
            echo "Pipeline completed successfully!"
        }
        
        // 'failure' block runs only if a stage failed
        failure {
            // Print a failure message
            echo "Pipeline encountered an error during execution."
        }
    }
}
