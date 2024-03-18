# EyeVoted Project

## Overview
EyeVoted is a project aimed at enhancing the voting process using iris recognition technology. It provides a secure and efficient way for users to cast their votes in elections.

## Project Structure
The project consists of several modules and utilities:

- **src/lib**: Contains the main application code, including models, views, controllers, services, and utilities.
  - `models`: Data models such as User, Vote, Candidate.
  - `views`: User interface screens like LoginScreen, VotingScreen, ResultsScreen.
  - `controllers`: Classes responsible for handling user actions and business logic.
  - `services`: Services for authentication, external APIs integration (e.g., Blockchain).
  - `utils`: Utility functions and constants used throughout the application.
- **src/assets**: Contains images and icons used in the application.
- **src/test**: Test files for widget and unit testing.
- **docs**: Documentation files including setup guide and API documentation.
- **ci_cd/.github/workflows**: Continuous integration and deployment workflows.
- **iris_auth**: Module for iris recognition functionalities.
  - `capture`: Functions for capturing iris images.
  - `preprocessing`: Preprocessing steps for iris images.
  - `feature_extraction`: Feature extraction techniques.
  - `matcher`: Matching algorithms for iris recognition.
  - `utils`: Utility functions for iris recognition module.

## Usage
To use the EyeVoted project, follow these steps:
1. Clone the repository: `git clone https://github.com/eyevoted/eyevoted.git`
2. Install dependencies: `cd eyevoted && pip install -r requirements.txt`
3. Run the application: `python main.py`

## Contribution
Contributions to the EyeVoted project are welcome! Feel free to submit pull requests for bug fixes, new features, or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
