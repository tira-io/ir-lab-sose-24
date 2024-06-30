import * as topics from './topics.json'
import * as example_documents from './example-documents.json'
import * as runs from './run_overview.json'

export default topics

let data_access = {
'databases': {
    'ir-lab-sose-2024/ir-acl-anthology-20240504-training': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-sose-2024/ir-lab-sose-2024.db',
    'ir-lab-sose-2024/ir-acl-anthology-topics-koeln-20240614-in-progress-test': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-sose-2024/ir-lab-sose-2024.db',
    'ir-lab-sose-2024/ir-acl-anthology-topics-augsburg-20240525_0-test': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-sose-2024/ir-lab-sose-2024.db',
    'ir-lab-sose-2024/ir-acl-anthology-topics-leipzig-20240423-test': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-sose-2024/ir-lab-sose-2024.db',
  },
  'documents': {
    'ir-lab-sose-2024/ir-acl-anthology-20240504-training': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-sose-2024/inputs/documents.jsonl',
    'ir-lab-sose-2024/ir-acl-anthology-topics-koeln-20240614-in-progress-test': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-sose-2024/inputs/documents.jsonl',
    'ir-lab-sose-2024/ir-acl-anthology-topics-augsburg-20240525_0-test': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-sose-2024/inputs/documents.jsonl',
    'ir-lab-sose-2024/ir-acl-anthology-topics-leipzig-20240423-test': 'https://files.webis.de/data-in-progress/dataset-explorer-in-progress/ir-lab-sose-2024/inputs/documents.jsonl',
  }
}

export { data_access, example_documents, runs }