import {filter_topics, uniqueElements} from '../utils'

let TOPICS_FOR_TEST = [
    {'dataset': 'd', 'query_id': 'q', 'default_text': 't'},
    {'dataset': 'd', 'query_id': 'q1', 'default_text': 't'}, 
    {'dataset': 'e', 'query_id': 'q3', 'default_text': 't'}
]


test('Unique elements of dataset', () => {
    expect(uniqueElements(TOPICS_FOR_TEST, 'dataset') + '').toBe('d,e')
})

test('Method filter_topics filters nothing by default', () => {
    expect(filter_topics(TOPICS_FOR_TEST).length).toBe(TOPICS_FOR_TEST.length)
})

test('Method filter_topics filters single query', () => {
    expect(filter_topics(TOPICS_FOR_TEST, 'q').length).toBe(1)
    expect(filter_topics(TOPICS_FOR_TEST, 'q')[0]['query_id']).toBe('q')
})

test('Method filter_topics filters multiple queries', () => {
    expect(filter_topics(TOPICS_FOR_TEST, 'q,q3').length).toBe(2)
    expect(filter_topics(TOPICS_FOR_TEST, 'q,q3')[0]['query_id']).toBe('q')
    expect(filter_topics(TOPICS_FOR_TEST, 'q,q3')[1]['query_id']).toBe('q3')
})

test('Method filter_topics filters single dataset', () => {
    expect(filter_topics(TOPICS_FOR_TEST, null, 'd').length).toBe(2)
    expect(filter_topics(TOPICS_FOR_TEST, null, 'd')[0]['dataset']).toBe('d')
    expect(filter_topics(TOPICS_FOR_TEST, null, 'd')[1]['dataset']).toBe('d')
})

test('Method filter_topics filters multiple datasets', () => {
    expect(filter_topics(TOPICS_FOR_TEST, null, 'd,e').length).toBe(TOPICS_FOR_TEST.length)
})

test('Method filter_topics filters by query datasets', () => {
    expect(filter_topics(TOPICS_FOR_TEST, null, null, 't').length).toBe(TOPICS_FOR_TEST.length)
})

test('Method filter_topics filters by query lowercase datasets', () => {
    expect(filter_topics(TOPICS_FOR_TEST, null, null, 'T').length).toBe(TOPICS_FOR_TEST.length)
})

test('Method filter_topics filters by non-existing query datasets', () => {
    expect(filter_topics(TOPICS_FOR_TEST, null, null, 'does-not-exist').length).toBe(0)
})

test('Method with multiple filters single dataset.', () => {
    expect(filter_topics(TOPICS_FOR_TEST, 'q,q3', 'd').length).toBe(1)
    expect(filter_topics(TOPICS_FOR_TEST, 'q,q3', 'd')[0]['query_id']).toBe('q')
})


test('Method with multiple filters multiple dataset.', () => {
    expect(filter_topics(TOPICS_FOR_TEST, 'q,q3', 'd,e').length).toBe(2)
    expect(filter_topics(TOPICS_FOR_TEST, 'q,q3', 'd,e')[0]['query_id']).toBe('q')
    expect(filter_topics(TOPICS_FOR_TEST, 'q,q3', 'd,e')[1]['query_id']).toBe('q3')
})

