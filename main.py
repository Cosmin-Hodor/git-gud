#!/usr/bin/env python3
import argparse
from datetime import datetime, timedelta
from random import randint
import os
import subprocess

def run(cmd):
    subprocess.run(cmd, check=True)

def commit(date):
    with open('README.md', 'a') as f:
        f.write(f'Contribution: {date.strftime("%Y-%m-%d %H:%M")}\n\n')
    run(['git', 'add', '.'])
    run(['git', 'commit', '-m', f'"{date.strftime("%Y-%m-%d %H:%M")}"', 
         '--date', date.strftime('%Y-%m-%d %H:%M:%S')])

def main(repo, days=365, freq=80, max_daily=10, no_weekends=False):
    os.makedirs(repo, exist_ok=True)
    os.chdir(repo)
    run(['git', 'init'])

    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    for day in (start_date + timedelta(n) for n in range(days)):
        if (not no_weekends or day.weekday() < 5) and randint(1, 100) <= freq:
            for _ in range(randint(1, max_daily)):
                commit_time = day + timedelta(minutes=randint(0, 1439))
                commit(commit_time)

    print("Local repository created successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Git repository with a commit history.")
    parser.add_argument('repo', help="Name of the repository to create")
    parser.add_argument('-d', '--days', type=int, default=365, help="Number of days to generate commits for")
    parser.add_argument('-f', '--frequency', type=int, default=80, help="Percentage of days to commit")
    parser.add_argument('-m', '--max-daily', type=int, default=10, help="Maximum commits per day")
    parser.add_argument('-nw', '--no-weekends', action='store_true', help="Skip weekends")
    args = parser.parse_args()

    main(args.repo, args.days, args.frequency, args.max_daily, args.no_weekends)