
import { data_access } from "@/ir_datasets"
import { execute_get } from "@/utils"
import { createDbWorker } from "sql.js-httpvfs"

const workerUrl = new URL(
  "sql.js-httpvfs/dist/sqlite.worker.js",
  import.meta.url,
);

const wasmUrl = new URL(
  "sql.js-httpvfs/dist/sql-wasm.wasm",
  import.meta.url,
);

export async function load_document_offsets(ir_dataset: 'ir-lab-sose-2024/ir-acl-anthology-20240504-training', doc_id: string) {
  if (!(ir_dataset in data_access.databases)) {
    return {'text': 'Dataset "' + ir_dataset + '" is not supported.'}
  }

  const maxBytesToRead = 10 * 1024 * 1024;
  const worker = await createDbWorker(
    [{from: "inline", config: {serverMode: "full", requestChunkSize: 1024, url: data_access.databases[ir_dataset]}}],
    workerUrl.toString(),
    wasmUrl.toString(),
    maxBytesToRead
  )

  let result = await worker.db.exec(`select * from documents where id = ?`, [doc_id])//[0]['values'];
  if (result.length == 0) {
    console.log('Could not find the document id ' + doc_id)
    throw new Error('Could not find the document id' + doc_id);
  }
  result = result[0]['values'][0]
  return {'start': result[1], 'end': result[2] -1}
}

export async function load_document(ir_dataset: 'ir-lab-sose-2024/ir-acl-anthology-20240504-training', doc_id: string) {
    let offsets = await load_document_offsets(ir_dataset, doc_id)

    return await execute_get(data_access.documents[ir_dataset], offsets['start'] + '-' + offsets['end'])
  }