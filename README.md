# Upwork RSS Feed Notifier

## Overview

The Upwork RSS Feed Notifier is a Python application that automatically checks the RSS feed of the Upwork website for new projects and sends notifications to Telegram using a bot. Additionally, it provides a feature to translate the project descriptions into a selected language.

## Features

- **RSS Feed Monitoring**: Continuously monitors the Upwork RSS feed to identify new projects and changes.

- **Telegram Integration**: Sends real-time project notifications to a Telegram bot, keeping you updated on new opportunities.

- **Translation**: Translates project descriptions into a language of your choice, enabling you to read project details in your preferred language.

- **Customizable**: Easily configure the RSS feed, notification settings, and translation preferences according to your needs.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed.
- Set up a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
    ```

- Install the required packages using `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/upwork-rss-notifier.git
    ```

2. Configure the application settings, such as RSS feed URL, Telegram bot API token, and translation preferences, in the `config.py` file.

3. Run the application:

    ```bash
    python app.py
    ```

4. The application will automatically check the Upwork RSS feed, send notifications to your Telegram bot, and translate project descriptions if desired.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository on GitHub.
2. Create a new branch from the main branch.
3. Make your changes and commit them with clear commit messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Upwork for providing an RSS feed for project listings.
- Special thanks to contributors and users who help improve this application.

---

Stay updated on Upwork projects with real-time notifications and translation capabilities! 🌐📢

**Viktor Andreev**
**and.viktor@gmail.com**
