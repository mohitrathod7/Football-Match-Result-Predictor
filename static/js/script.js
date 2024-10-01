function changeTeamImage(section) {
    const selectElement = document.getElementById(section + '_name');
    const selectedOption = selectElement.options[selectElement.selectedIndex];
    const logoFileName = selectedOption.getAttribute('data-logo');
    const logoElement = document.getElementById(section + '-logo');
    
    // Update the image source
    logoElement.src = "{{ url_for('static', filename='img/team_logos/') }}" + logoFileName;
}