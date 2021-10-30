/*Full blog page*/
document.getElementById('show').style.display = 'none';

document.getElementsByClassName('delete')[0].addEventListener('click', function() {
    document.querySelector('#options').style.display = 'none';
    document.querySelector('#show').style.display = 'inline';
});