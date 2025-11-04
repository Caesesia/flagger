import subprocess
import json

def show_team(team_id: str) -> str:

    url = f'https://ctftime.org/api/v1/teams/{team_id}'

    cmd = subprocess.run(['curl', '-s', url], capture_output = True, text = True)
    
    try:
        data = json.loads(cmd.stdout)
        return data

    except json.JSONDecodeError:
        print("Invalid JSON response:")
        print(cmd.stdout)
        return None

    return None
