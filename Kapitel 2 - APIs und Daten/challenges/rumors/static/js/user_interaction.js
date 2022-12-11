function spread(rumor_id){
$.ajax({
    url: '/spread/'+rumor_id,
    type: 'PUT',
    success: function(result) {
        $("#"+rumor_id).html("<i style=\"cursor: pointer;\" onclick=\"spread('"+rumor_id+"')\" class=\"bi bi-share text-danger\">  "+result['propagated']+"</i>");
    }
});
}

function love(rumor_id){
$.ajax({
    url: '/love/'+rumor_id,
    type: 'PUT',
    success: function(result) {
        $("#hearted_"+rumor_id).html("<i style=\"cursor: pointer;\" onclick=\"love('"+rumor_id+"')\" class=\"bi bi-arrow-through-heart text-danger\">  "+result['loved']+"</i>");
    }
});
}