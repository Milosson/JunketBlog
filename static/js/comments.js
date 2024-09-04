const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment` endpoint with the comment ID.
 */
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;

    // Populate the comment text area with the existing comment content
    commentText.value = commentContent;

    // Change the submit button text to "Update"
    submitButton.innerText = "Update";

    // Update the form's action URL to point to the comment edit view
    const postSlug = window.location.pathname.split('/')[2]; // Get the post slug from the URL
    commentForm.setAttribute("action", `/post/${postSlug}/edit-comment/${commentId}/`);
  });
}
