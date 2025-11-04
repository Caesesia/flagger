import subprocess
import json

def list_events(number: str, time_start: str, time_stop: str) -> str:

    url = f'https://ctftime.org/api/v1/events/?limit={number}&start={time_start}&finish={time_stop}'
    cmd = subprocess.run(['curl', '-s', url], capture_output = True, text = True)
    
    try:
        data = json.loads(cmd.stdout)
        print(data)
        return data

    except json.JSONDecodeError:
        print("Invalid JSON response:")
        print(cmd.stdout)
        return None

    return None



def show_event(event_id: str):

    url = f'https://ctftime.org/api/v1/events/{event_id}'
    cmd = subprocess.run(['curl', '-s', url], capture_output = True, text = True)
    
    try:
        data = json.loads(cmd.stdout)
        print(data)
        return data

    except json.JSONDecodeError:
        print("Invalid JSON response:")
        print(cmd.stdout)
        return None

    return None
