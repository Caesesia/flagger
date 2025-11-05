import subprocess
import json
from utils.date_to_unix import convert_time

def list_events(number: str, start: str, finish: str):

    start, finish = convert_time(start, finish)

    url = f'https://ctftime.org/api/v1/events/?limit={number}&start={start}&finish={finish}'
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
