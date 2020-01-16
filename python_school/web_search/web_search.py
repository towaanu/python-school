import random
import matplotlib.pyplot as plt

def display_result(site_stats):
    x_labels = list(site_stats.keys())

    bar_values = [site_stats[key]['visit'] for key in site_stats.keys()]

    plt.bar(x_labels, bar_values)
    plt.savefig('./sites_stats.png')
    plt.clf()
    
def custom_crawler(websites, nb_tests=30):
    random.seed()

    site_labels = list(websites.keys())
    start_site_index = random.randint(0, 3)
    start_site = site_labels[start_site_index]

    visited_values = {}
    for label in site_labels:
        visited_values[label] = 0

    # visited_values[start_site] = 1

    current_site = websites[start_site]
    current_site_label = start_site

    for i in range(nb_tests):
        count_links = len(current_site)

        if count_links > 0:
            next_site_index = random.randint(0, count_links - 1)
            current_site_label = current_site[next_site_index]['to']
            current_site = websites[current_site_label]

        visited_values[current_site_label] += 1
    
    visited_stats = {}
    for key in visited_values:
        nb_visits = visited_values[key]
        visited_stats[key] = {
            'visit': nb_visits,
            'percentage': (nb_visits / nb_tests) * 100,
            'fraction': f"{nb_visits}/{nb_tests}"
        }

    return visited_stats
    
if __name__ == "__main__":
    print("Hello web search")

    websites = {
        "A": [{'to': 'B'}, {'to': 'C'}, {'to': 'D'}],
        "B": [{'to': 'A'}, {'to': 'D'}],
        "C": [{'to': 'D'}, {'to': 'A'}, {'to': 'E'}],
        "D": [{'to': 'B'}, {'to': 'C'}],
        "E": [{'to': 'A'}]
    }

    sites_stats = custom_crawler(websites, 1000)
    display_result(sites_stats)
    print(sites_stats)