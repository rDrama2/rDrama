function togglePostEdit(id){
	body=document.getElementById("post-body");
	title=document.getElementById("post-title");
	form=document.getElementById("edit-post-body-"+id);

	body.classList.toggle("d-none");
	title.classList.toggle("d-none");
	form.classList.toggle("d-none");

	box=document.getElementById("post-edit-box-"+id);
	autoExpand(box);
	box=document.getElementById("post-edit-title");
	autoExpand(box);
};
