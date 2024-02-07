/* Stefan's JS*/


document.addEventListener('DOMContentLoaded', function () {
    // Get the src attribute from the img tag
    const imgSrc = document.getElementById('bookCover').src;

    // Extract the ISBN from the imgSrc using a regular expression
    const isbnMatch = imgSrc.match(/\/isbn\/(\d+)\.jpg/);

    // Check if a match is found
    if (isbnMatch && isbnMatch[1]) {
        const isbn = isbnMatch[1];
        const apiUrl = `https://openlibrary.org/isbn/${isbn}.json`;

        fetch(apiUrl)
            .then(response => response.json())
            .then(data => {
                const title = data.title;
                document.getElementById('bookTitle').innerHTML = `Title: ${title}`;
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                document.getElementById('bookTitle').innerHTML = 'Error fetching data. Please try again later.';
            });
    } else {
        console.error('ISBN not found in the img src attribute.');
        document.getElementById('bookTitle').innerHTML = 'Error: ISBN not found.';
    }
});
