ckan.module('query_form', function($, _) {
    return {
        initialize: function() {
            var showingQuery = false;
            //get the default action
            var action = document.getElementById('resource-edit').action
            var queryAction = action;
            var normalAction = action;
            //if we are on the add new_resource page then set the query action to be new with id instead of new_resoure
            if (action.indexOf("new_resource") > 0) {
                //queryAction = queryAction.replace("new_resource/", "new?id=");
		              queryAction = queryAction.replace("dataset/new_resource/", "ssb?id=");
		//console.log(queryAction);
            }

            //if we are on the edit resource page then set the hidden resourceID input field to contain the resource id extracted from the action url which enables it to be sent with the form
            //set the query action to the same as it would be if called from the new_resource page. Routing the calls to the same controller action(new_resource_ssb)
            if (action.indexOf("resource_edit") > 0) {
                var resourceID = action.substring(action.indexOf("resource_edit") + 14, action.length);
                document.getElementById('resourceid').value = resourceID;

                queryAction = action.substring(0, action.indexOf("dataset"));
                queryAction = queryAction + "ssb?id=" + action.substring(action.indexOf("dataset") + 8, action.indexOf("resource_edit") - 1);
            }

            //on click toggle between query input and url/file input
            $('#form-toggle').on('click', function() {http://localhost/dataset/supertest/resource_edit/db69493f-7d9a-47dd-b8bd-ca3d562c2980
                if (showingQuery) {
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
