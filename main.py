import base64
import json
from google.cloud import bigquery

def dataplex_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic for BQ load job completed events.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    bq_client = bigquery.Client()

    # process pubsub message, message payload (event) is a dict with the attribute data as a base64 encoded string
    # so event['data'] need to be decoded first to obtain a json string, then converted to dict with json.loads()
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    data = json.loads(pubsub_message)

    print("============= Event ==============")
    print(event)

    print("============= Context ==============")
    print(context)

    print("============= Data ==============")
    print(data)

    # # the attributes being accessed here is dependent on the message being routed from log
    # project_id = data['protoPayload']['serviceData']['jobCompletedEvent']['job']['jobConfiguration']['load']['destinationTable']['projectId']
    # dataset_id = data['protoPayload']['serviceData']['jobCompletedEvent']['job']['jobConfiguration']['load']['destinationTable']['datasetId']
    # table_id = data['protoPayload']['serviceData']['jobCompletedEvent']['job']['jobConfiguration']['load']['destinationTable']['tableId']

    # # get table object and schema from payload data
    # table_ref = f"{project_id}.{dataset_id}.{table_id}"
    # target_table = bq_client.get_table(table_ref)
    # table_schema = target_table.schema

    # dataplex = DataplexService.DataplexService(project_id, dataset_id, table_id)

    # # search for asset on project_id, with type table, and tag any.
    # search_string = f"projectid={project_id} AND type=table AND tag:"
    # for res in dataplex.lookup_tables(search_string):
    #     tag_to_apply = dataplex.generate_tag_to_apply(
    #         parent=res.relative_resource_name, table_schema=table_schema
    #     )

    # # apply tags for matching columns if any
    # for tag in tag_to_apply:
    #     applied_tag = dataplex.apply_tag(*tag)
    
    # # apply policy tag if necessary
    # if applied_tag.fields['email_sensitivity'].enum_value.display_name != "Public":
    #     policy_tags=bigquery.PolicyTagList([dataplex.get_policy_tag()])

    #     target_table.schema = [
    #         bigquery.SchemaField(
    #             name=schema_field.name,
    #             field_type=schema_field.field_type,
    #             mode=schema_field.mode,
    #             policy_tags=policy_tags
    #         )
    #         if schema_field.name == applied_tag.column else schema_field for schema_field in table_schema
    #     ]

    #     target_table = bq_client.update_table(target_table, ["schema"])

    # # add table to zone entity
    # # entity = dataplex.add_entity()

    # # generate cloud dq config, then run/schedule the task
    # bucket_name = "<BUCKET-NAME>"
    # if applied_tag.template == "projects/<PROJECT-ID>/locations/asia-southeast2/tagTemplates/<TAG-TEMPLATE-NAME>":
    #     config_path = dataplex.generate_dq_config(applied_tag.column, bucket_name)

    # result = dataplex.create_dq_task(config_path)
    # print(result)