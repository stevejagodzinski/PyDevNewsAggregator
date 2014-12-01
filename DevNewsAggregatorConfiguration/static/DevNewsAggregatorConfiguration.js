$('.make-switch').on('switchChange.bootstrapSwitch', function (event, state) {
    var dataNewsSourceName = event.delegateTarget.getAttribute("data-news-source-name");
    if(state) {
        $.ajax("/DevNewsAggregatorConfiguration/html_content_user/add/"+ dataNewsSourceName + "/", {
            headers: {'X-CSRFToken': $.cookie('csrftoken')},
            type: "POST",
            success: handleContentAdded
        });
    } else {
        $("[data-content-source='" + dataNewsSourceName + "']").remove();

        $.ajax("/DevNewsAggregatorConfiguration/html_content_user/delete/"+ dataNewsSourceName + "/", {
            headers: {'X-CSRFToken': $.cookie('csrftoken')},
            type: "POST"
        });
    }
});

function addQuickSideBarAddEditClickHandler() {
    var quickSidebarItems = $('.page-quick-sidebar-wrapper .page-quick-sidebar .list-items > li');
    quickSidebarItems.click(function (e) {
        var target = $(e.target);
        if (target.is('li')) {
            var mousePosition = e.offsetX || e.clientX - target.offset().left;
            if (mousePosition >= 10 && mousePosition <= 27) {
                quickSidebarIconClicked(target);
            }
        }
    });
}

function quickSidebarIconClicked(target) {
    if(target.attr('id') == 'add-new-content-source') {
        handleAddClicked();
    } else {
        handleEditClicked(target);
    }
}

function handleAddClicked() {
    window.location.href = "/DevNewsAggregatorConfiguration/html_content/new/";
}

function handleEditClicked(target) {
    var htmlContentId = target.attr('data-news-source-id');
    window.location.href = "/DevNewsAggregatorConfiguration/html_content/" + htmlContentId + "/";
}

function handleContentAdded(content) {
    var contentContainer = $('.content');
    var existingNewsEntries = contentContainer.children('.news-entry');
    var newNewsEntries = $(content).children('.news-entry');

    var newNewsEntriesTraversalIndex = 0;

    for (var existingNewsEntriesTraversalIndex = 0; existingNewsEntriesTraversalIndex<existingNewsEntries.length && newNewsEntriesTraversalIndex<newNewsEntries.length; existingNewsEntriesTraversalIndex++) {
        var existingNewsEntry = existingNewsEntries.eq(existingNewsEntriesTraversalIndex);

        // TODO: Set timezone on php server
        var existingNewsEntryDate = new Date(existingNewsEntry.find('.news-entry-date').attr('data-iso-date'));

        do{
            var inserted = false;
            // TODO: Don't run this jquery every time
            var newNewsEntry = newNewsEntries.eq(newNewsEntriesTraversalIndex);
            var newNewsEntryDate = new Date(newNewsEntry.find('.news-entry-date').attr('data-iso-date'));
            if(newNewsEntryDate > existingNewsEntryDate) {
                newNewsEntry.insertBefore(existingNewsEntry);
                inserted = true;
                newNewsEntriesTraversalIndex++;
            }
        }while(inserted);
    }

    for(var i=newNewsEntriesTraversalIndex; i<newNewsEntries.length; i++) {
        contentContainer.append(newNewsEntries.get(i));
    }
}