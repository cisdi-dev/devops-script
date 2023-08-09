import yaml
import argparse
from dotenv import load_dotenv
import os

if __name__ == '__main__':
  msg = "Open API Spec Reformatter for API Gateway"
  parser = argparse.ArgumentParser(description=msg)
  parser.add_argument("-i", "--input-file", help="Path to OpenAPI spec yaml file")
  parser.add_argument("-e", "--env", help="Deployment Environment")
  args = parser.parse_args()
  load_dotenv(".env.{}".format(args.env))
  
  with open(args.input_file, 'r') as file:
    api_spec = yaml.safe_load(file)
  api_spec["info"]["title"] = "API Cisdi Talenta Integrations"
  api_spec["info"]["description"] = "Integrasi data Talenta dan CISDI"
  api_spec["info"]["version"] = "1.0.0"
  api_spec["x-google-backend"] = {'address': os.getenv("API_URL")}
  api_spec["schemes"] = ['https']
  api_spec["produces"] = ['application/json']
  for x in api_spec["paths"]:
    for y in api_spec["paths"][x]:
      api_spec["paths"][x][y]["operationId"] = api_spec["paths"][x][y]["description"][0].lower() + api_spec["paths"][x][y]["description"].replace(" ", "").replace("'","")[1:]
      api_spec["paths"][x][y]["security"] = [{'api_key_header': []}]
  api_spec["securityDefinitions"]["api_key_header"] = {
    "type": "apiKey",
    "name": "x-api-key",
    "in": "header"
  }
  api_spec["securityDefinitions"]["api_key_query"] = {
    "type": "apiKey",
    "name": "key",
    "in": "query"
  }
  
  del api_spec["securityDefinitions"]["JWT"]
  
  with open("api_gateway_spec.yaml", 'w') as file:
    yaml.dump(api_spec, file)
  print(api_spec)

