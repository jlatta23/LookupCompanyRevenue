var results_index = 0;
        var order_column = "revenue_estimate-column";
        var order_direction = "desc";
        $(document).ready(function(){
            $("#searchBusinessSubmit").click(function(){
                results_index = 0;
                searchBusinesses(results_index);
            });


            $(".sel").on("keydown", function(e){                
                if (e.code == "Enter"){
                    results_index = 0;
                    searchBusinesses(results_index);       
                }
            });

            
            $("#resetSearchParameters").click(function(){
                $("#companyName").val("");
                $("#industry").val("");
                $("#zipCode").val("");
                $("#revenueRange").val("Any");
                $("#employeeRange").val("Any");
                $("#states").val("Any");
            });

            $("#nextButton").click(function(){
                results_index = results_index + 1;
                searchBusinesses(results_index);
            });

            $("#prevButton").click(function(){
                results_index = results_index - 1;
                searchBusinesses(results_index);
            });

            $(".sortable-column").click(function(event) {
                $(this).attr("style","border:1px solid black;background-color:#acb6c2;");
                $(".sortable-column").not(this).find("img").attr("src", "{% static 'icons/up_down_column.svg' %}");
                $(".sortable-column").not(this).attr("style","");
                if(order_column == $(this).attr("id")){
                    if(order_direction == "desc"){
                        $(this).find("img").attr("src", "{% static 'icons/arrow-up.svg' %}");
                        order_direction = "asc";
                    }
                    else{
                        $(this).find("img").attr("src", "{% static 'icons/arrow-down.svg' %}");
                        order_direction = "desc";
                    }
                }
                else{
                    $(this).find("img").attr("src", "{% static 'icons/arrow-down.svg' %}");
                    order_direction = "desc";
                }
                order_column = $(this).attr("id");
                if(order_column == null){
                    alert("how is this null you numb nuts " + $(this).attr("id"));
                }
                

                results_index = 0;
                searchBusinesses(results_index);

            
            });
            $(".business-span").click(function(event){
               window.location.href = $(event.target).attr("href");
            });
        });

function updatePrevNextButtons(){
            
    if(results_index == 0){
        $("#prevButton").prop('disabled', true);
    }
    else{
        $("#prevButton").prop('disabled', false);
    }
};

function goToBusiness(url){
    window.location.href = url;
}

function searchBusinesses(start_index){
    var s = '<div class="spinner-border text-primary" role="status" id="tableSpinner"> <span class="visually-hidden">Loading...</span></div>';
    $("#tableSpinner").html(s);
    if(order_column == null){
        //alert("order col null!");
    }
    
    $.ajax({
        url:"/search",
        type:"GET",
        data: {"companyName":$("#companyName").val(),
            "zipCode":$('#zipCode').val(),
            "industry":$('#industry').val(),
                "revenueRange":$('#revenueRange option:selected').val(),
            "employeeRange":$('#employeeRange option:selected').val(),
            "state":$('#states option:selected').val(),
            "start_index":start_index,
            "order_by":order_column,
            "order_dir":order_direction},
    success: function(response){
        html = response; //response["html"];            
        //num_businesses = response["num_businesses"];
        $("#tableSpinner").html('');
        $("#resultBusinesses").find("tbody").html(html);
        updatePrevNextButtons();
        $(".business-row").click(function(event){
            window.location = $(this).data("href");
        });
        //$("#numBusinesses").html("Number of businesses matching applied filters: " + num_businesses);
    }})
};