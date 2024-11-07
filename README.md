# 🌱 Git History Generator

A sleek Python tool to create local Git repositories with customizable commit histories. Perfect for testing, learning Git, or setting up demo projects!

## 🚀 Features

- 📅 Generate commits over a custom time range
- 🎲 Randomized commit frequency and volume
- 🏖 Option to exclude weekends
- 🛠 Highly customizable via command-line arguments

## 🛠 Installation

1. Ensure you have Python 3.6+ installed
2. Clone this repository:

`git clone https://github.com/Cosmin-Hodor/git-gud.git`
`cd git-gud`

3. Make the script executable:

`chmod +x main.py`

## 🏄‍♂️ Usage

Basic usage:

`./main.py my_awesome_repo`

This creates a new repository named `my_awesome_repo` with a year's worth of commits.

### 🎛 Advanced Options

Customize your repository generation with these options:

- `-d, --days`: Number of days to generate commits for (default: 365)
- `-f, --frequency`: Percentage of days to commit (default: 80)
- `-m, --max-daily`: Maximum commits per day (default: 10)
- `-nw, --no-weekends`: Skip generating commits on weekends

Example with all options:

`./git_history_generator.py epic_project -d 180 -f 70 -m 5 -nw`

This creates `epic_project` with:
- Commits spanning the last 180 days
- Commits on 70% of the days
- Up to 5 commits per day
- No commits on weekends

## 🌟 Why Use Git History Generator?

- 🎓 Perfect for Git tutorials and workshops
- 🧪 Test Git-based tools and integrations
- 🎨 Create visually appealing Git histories for demos
- 🏋️ Practice Git operations on repos with substantial history

## ⚠️ Ethical Note

This tool is designed for educational and testing purposes. Please use responsibly and avoid using it to misrepresent development activity in public repositories.

## 🙏 Acknowledgements

- Inspired by the [github-activity-generator.git](https://github.com/Shpota/github-activity-generator/tree/main) and the spirit of open-source
- Built with love for developers and Git enthusiasts worldwide

---

Happy Coding! 🚀👨‍💻👩‍💻
