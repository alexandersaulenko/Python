# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, StatusMessage, FunctionResult, FunctionError
import co3 as resilient

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function(s)"""

    @function("get_all_artifacts_of_incident")
    def _get_all_artifacts_of_incident_function(self, event, *args, **kwargs):
        """Function: Retrieves all Artifacts of an Incident, and returns them in raw dictionary."""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            
            yield StatusMessage("starting...")
            # This part is for initializing the Resilient REST API client
            
            # This line gets the parser that will load and parse the app.config file.
            parser = resilient.ArgumentParser(config_file=resilient.get_config_file())
            
            # This line parses the arguments from the app.config file.
            opts = parser.parse_args()

            # Initialization of the Resilient REST API client
            client = resilient.get_client(opts)
            
            # Retrieve the artifacts endpoint, which returns a list of artifacts
            artifacts = client.get("/incidents/{0}/artifacts".format(incident_id))

            yield StatusMessage("done...")
            
            # Since Function results must be a Dictionary, and not a list, this format is used to pass the list of artifacts.
            results = {"artifacts":artifacts}

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
