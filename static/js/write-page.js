$(document).ready(function () {
// Placeholder behavior
$(".title, .subtitle, .content").on("focus", function () {
if ($(this).text() === "Title" || $(this).text() === "Add a subtitle..." || $(this).text() === "Start writing...") {
$(this).text("").css("color", "#333");
}
});

// Bold & Italic Formatting
function formatText(command) {
document.execCommand(command, false, null);
}

// Add Link
function addLink() {
let url = prompt("Enter the link URL:");
if (url) document.execCommand("createLink", false, url);
}

// Add Image
function addImage() {
let imageUrl = prompt("Enter image URL:");
if (imageUrl) {
document.execCommand("insertImage", false, imageUrl);
}
}

// Add Lists
function addList(type) {
let command = type === "ul" ? "insertUnorderedList" : "insertOrderedList";
document.execCommand(command, false, null);
}

// Bind button actions
$("button").click(function () {
let action = $(this).attr("onclick");
if (action) eval(action); // Executes function based on button click
});
});
