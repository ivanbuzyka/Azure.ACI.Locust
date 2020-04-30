# Azure.ACI.Locust

ARM template and guides for deployment and running of distributed Locust in Azure Container Instances

## Get started

### Prerequisites

#### Create an Azure file share

Locust need to access Python file with load testing script. For that reason we will use typical approach by mounting folder to the container by using Azure file share.
What needs to be done:

* create Azure Storage Account
* [create azure file share](https://docs.microsoft.com/en-us/azure/storage/files/storage-how-to-create-file-share?tabs=azure-cli)
* write down Azure Storage Key, storage account name and file share name which will be used in ARM template for container deployment.
* upload locust Python file (e.g. `simple-load.py` from this repository) to the root of the Azure File share

### Fill in parameters

Add parameter values to the `parameters.json` file

### Deploy ARM template

Example for running deployment by Azure CLI:

```bash
az group deployment create -g ibu-loadtesting --template-file "C:\path-to-repo\Azure.ACI.Locust\arm\template.json" --parameters "C:\path-to-repo\Azure.ACI.Locust\arm\parameters.json"
```

### Open locust UI

Find Hostname of the Locust master and open it in the browser.
Open master Container Group in the Azure Portal and copy hostname (`something.westeurope.azurecontainer.io`), open it in browser using port `8089`:

```url
http://something.westeurope.azurecontainer.io:8089
```

Locust has [great documentation](https://docs.locust.io/en/stable/quickstart.html#open-up-locust-s-web-interface) to get started with it

### Remove container groups when not needed

In order to save money, make sure to remove container groups or stop containers within them.
