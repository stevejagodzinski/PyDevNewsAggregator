$('.make-switch').on('switchChange.bootstrapSwitch', function (event, state) {
    if(!state) {
        var dataNewsSourceName = event.delegateTarget.getAttribute("data-news-source-name");
        $("[data-content-source='" + dataNewsSourceName + "']").remove();

        $.ajax("/DevNewsAggregatorConfiguration/html_content_user/delete/"+ dataNewsSourceName + "/", {
            headers: {'X-CSRFToken': $.cookie('csrftoken')},
            type: "POST"
        });
    }
});