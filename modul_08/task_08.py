from collections import Counter


def get_count_visits_from_ip(ips):
    return dict(Counter(ips))


def get_frequent_visit_from_ip(ips):

    return Counter(ips).most_common(1)[0]


ip_addresses = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '10.0.0.1', 
                '10.0.0.2', '192.168.1.3', '172.16.0.1', '192.168.1.2', 
                '192.168.1.3', '192.168.1.1']

print(get_count_visits_from_ip(ip_addresses))

print(get_frequent_visit_from_ip(ip_addresses))