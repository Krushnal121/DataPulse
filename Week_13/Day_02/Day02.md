### Day 2: Azure Functions
---
**Overview:**
- **Topic:** Azure Functions
- **Objective:** Understand the basics of serverless computing and how to create and deploy Azure Functions.

**Key Concepts:**
- **Triggers and Bindings:** Explore how Azure Functions can be triggered by various events such as HTTP requests, timers, or messages.
- **Development and Deployment:** Learn how to develop Azure Functions locally and deploy them to the cloud.
- **Scaling:** Understand how Azure Functions scale automatically based on demand.

**Code Snippet:**
```python
import azure.functions as func
import logging

# Example: HTTP-triggered Azure Function
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}!")
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body.",
            status_code=400
        )
```