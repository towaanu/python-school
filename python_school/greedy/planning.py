import matplotlib.pyplot as plt
import random

def display_planning(activities, file_name="planning.png"):
    plt.ylabel("Activities")
    plt.xlabel("Time")

    for i in range(len(activities)):
        (begin_hour, end_hour, color) = activities[i]
        plt.barh(i, end_hour - begin_hour, left=[begin_hour], height=0.4, color=color)
    
    plt.savefig(file_name)
    plt.clf()

def generate_planning(activities):
    sorted_activities = sorted(activities, key= lambda a : a[1])
    last_activity = None
    planning = []
    for activity in sorted_activities:
        (begin_hour, end_hour, _color) = activity

        if last_activity is None or begin_hour >= last_activity[1]:
            planning.append(activity)
            last_activity = activity

    return planning

def generate_random_activities(nb_activities):
    random.seed()

    rand_activities = []
    for i in range(nb_activities):
        begin_hour = random.randrange(0, 23)

        if begin_hour == 23:
            end_hour = 24
        else:
            end_hour = random.randrange(begin_hour + 1, 24)

        red = random.randrange(0, 255) / 255
        green = random.randrange(0, 255) / 255
        blue = random.randrange(0, 255) / 255

        new_activity = (begin_hour, end_hour, (red, green, blue))

        rand_activities.append(new_activity)
    
    return rand_activities

if __name__ == "__main__":
    print("Hello planning :D")

    # activities = [(1, 5), (2, 5), (1, 2), (3, 4)]
    activities = generate_random_activities(10)
    display_planning(activities, "activities.png")

    res_planning = generate_planning(activities)
    display_planning(res_planning, "planning.png")
    print(f"Res planning {res_planning}")