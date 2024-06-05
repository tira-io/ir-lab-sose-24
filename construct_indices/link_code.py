#!/usr/bin/env python3
from requests import get
import json
from tqdm import tqdm

SYSTEMS = [
    "ir-lab-jena-leipzig-wise-2023/geometric-tortoise/silent-fork",
    "ir-lab-jena-leipzig-wise-2023/geometric-tortoise/rounded-teak",
    "ir-lab-jena-leipzig-wise-2023/geometric-tortoise/clear-solenoid",
    "ir-lab-jena-leipzig-wise-2023/geometric-tortoise/nippy-skin",
    "ir-lab-jena-leipzig-wise-2023/geometric-tortoise/recent-cordon",
    "ir-lab-jena-leipzig-wise-2023/geometric-tortoise/fast-upload",
    'ir-lab-jena-leipzig-wise-2023/ul-lucid-lovelace/resultant-associate',
    'ir-lab-jena-leipzig-wise-2023/ul-lucid-lovelace/cyan-comptroller',
    'ir-lab-jena-leipzig-wise-2023/ul-lucid-lovelace/rapid-ketchup',
    'ir-lab-jena-leipzig-wise-2023/ul-lucid-lovelace/spicy-chianti',
    'ir-lab-jena-leipzig-wise-2023/ul-lucid-lovelace/mashed-demon',
    'ir-lab-jena-leipzig-wise-2023/ul-trusting-neumann/auburn-land',
    'ir-lab-jena-leipzig-wise-2023/ul-hungry-ramanujan/plain-pool',
    'ir-lab-jena-leipzig-wise-2023/ul-dreamy-zuse/chief-walk',
    'ir-lab-jena-leipzig-wise-2023/ul-dreamy-zuse/caramelized-callable',
    'ir-lab-jena-leipzig-wise-2023/ul-dreamy-zuse/pureed-sack',
    'ir-lab-jena-leipzig-wise-2023/ul-dreamy-zuse/fundamental-wrap',
    "ir-lab-jena-leipzig-wise-2023/galapagos-tortoise/null-strait",
    "ir-lab-jena-leipzig-wise-2023/galapagos-tortoise/mild-duck",
    "ir-lab-jena-leipzig-wise-2023/galapagos-tortoise/edible-status",
    "ir-lab-jena-leipzig-wise-2023/galapagos-tortoise/poky-claim",
    "ir-lab-jena-leipzig-wise-2023/ul-kangaroo-query-crew/merry-chrysler",
    "ir-lab-jena-leipzig-wise-2023/ul-ecstatic-dijkstra/parameter-05",
    "ir-lab-jena-leipzig-wise-2023/ul-ecstatic-dijkstra/grim-engineer",
    "ir-lab-jena-leipzig-wise-2023/ul-ecstatic-dijkstra/parameter-50",
    "ir-lab-jena-leipzig-wise-2023/ul-ecstatic-dijkstra/recent-market",
    'ir-lab-jena-leipzig-wise-2023/ul-the-golden-retrievers/the-golden-retrievers-rev2',
    'ir-lab-jena-leipzig-wise-2023/ul-the-golden-retrievers/bo1-query-expansion',
    'ir-lab-jena-leipzig-wise-2023/ul-the-golden-retrievers/icy-guitar',
    'ir-lab-jena-leipzig-wise-2023/ul-nostalgic-turing/moderato-order',
    'ir-lab-jena-leipzig-wise-2023/ul-nostalgic-turing/succulent-scene',
    'ir-lab-jena-leipzig-wise-2023/ul-nostalgic-turing/dry-elbow',
    'ir-lab-jena-leipzig-wise-2023/spotted-turtle/proud-humanist',
    'ir-lab-jena-leipzig-wise-2023/spotted-turtle/fancy-department',
    'ir-lab-jena-leipzig-wise-2023/spotted-turtle/senile-portico',
    'ir-lab-jena-leipzig-wise-2023/spotted-turtle/bordeaux-bounce',
    'ir-lab-jena-leipzig-wise-2023/spotted-turtle/lead-pizza',
    'ir-lab-jena-leipzig-wise-2023/spotted-turtle/thick-major',
]

ret = {}
for i in tqdm(SYSTEMS):
    # make a python request
    response = get('https://www.tira.io/api/task/' + i.replace('-2023/', '-2023/submission-details/')).content.decode('UTF-8')
    response = json.loads(response)
    if 'context' not in response:
        continue
    response = response['context']['submission']

    if 'link_code' in response and response['link_code']:
        ret[i] = response['link_code']

json.dump(ret, open('ui/src/system-links.json', 'w'))