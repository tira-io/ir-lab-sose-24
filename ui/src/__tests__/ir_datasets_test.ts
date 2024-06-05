import topics from '../ir_datasets'

test('Topics can be imported and are defined.', () => {
    expect(topics).toBeDefined()
})

test('Topics are not empty and have a predefined set of properties.', () => {
    expect(topics[0]).toHaveProperty('dataset')
    expect(topics[0]).toHaveProperty('query_id')
    expect(topics[0]).toHaveProperty('default_text')
    expect(topics[0]).toHaveProperty('min_P@10')
    expect(topics[0]).toHaveProperty('run_details')
    expect(topics[0]).toHaveProperty('qrel_details')
})
