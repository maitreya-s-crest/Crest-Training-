# Owner: Maitreya Sapariya
# Project: Crest Training

def prioritize_tasks(tasks: list):
    prioritized = sorted(tasks, key=lambda x: len(x))
    return prioritized