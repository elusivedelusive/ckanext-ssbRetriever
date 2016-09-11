ckan.module('query_form', function($, _) {
    return {
        initialize: function() {
	    	var showingQuery = false;
		var action = document.getElementById('resource-edit').action
		var queryAction = action;
		var normalAction = action;
		if(action.indexOf("new_resource")>0){
			queryAction = queryAction.replace("new_resource/","new?id=") +document.getElementById('id').value;
		}

		if(action.indexOf("resource_edit") >0){
			var resourceID = action.substring(action.indexOf("resource_edit")+14, action.length);
			document.getElementById('resourceid').value = resourceID; 
			
			queryAction =  action.substring(0, action.indexOf("dataset")+8);
			queryAction = queryAction + "new?id=" +  action.substring(action.indexOf("dataset")+8, action.indexOf("resource_edit")-1);
		}
	
		console.log("action: " + action);
		console.log("normal action: " + normalAction);
		console.log("query  action: " + queryAction);
		console.log(action.indexOf("resource_edit"));
        	$('#form-toggle').on('click', function() {
			if(showingQuery){
				document.getElementById('field-query-url').value = "";
				document.getElementById('field-query-text').value = "";
				document.getElementById('field-image-url').value = " ";
				$('#query-inputs').hide();
				$('.image-upload').show();
				document.getElementById('resource-edit').action = normalAction;
				showingQuery = false;
			} else {
				$('#field_image_url').val("query");
				document.getElementById('field-image-url').value = " ";
				$('#query-inputs').show();
				$('.image-upload').hide();
				document.getElementById('resource-edit').action = queryAction
				showingQuery = true;
			}
        	});
    	}
    };
});
