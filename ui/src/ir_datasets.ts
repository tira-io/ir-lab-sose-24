import * as topics from './topics.json'
import * as example_documents from './example-documents.json'
import * as runs from './run_overview.json'

export default topics

let data_access = {
'databases': {
    'ir-lab-sose-2024/ir-acl-anthology-20240504-training': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-jena-leipzig-sose-2023/ir-lab-jena-leipzig-sose-2023.db'

  },
  'documents': {
    'ir-lab-sose-2024/ir-acl-anthology-20240504-training': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-jena-leipzig-sose-2023/inputs/documents.jsonl'
  }
}

export { data_access, example_documents, runs }