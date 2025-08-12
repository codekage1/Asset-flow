from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

# Data structures for storing information
projects_data = [
    {
        'id': 1,
        'title': 'Basketball Analytics Dashboard',
        'description': 'A comprehensive dashboard for analyzing basketball player statistics and team performance.',
        'technologies': ['Python', 'Flask', 'JavaScript', 'Chart.js'],
        'image': 'basketball.jpg'
    },
    {
        'id': 2,
        'title': 'Football Management System',
        'description': 'A web application for managing football team rosters, schedules, and match results.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'SQL'],
        'image': 'football.jpg'
    },
    {
        'id': 3,
        'title': 'MLF Data Platform',
        'description': 'A machine learning framework for data analysis and predictive modeling.',
        'technologies': ['Python', 'TensorFlow', 'Flask', 'API'],
        'image': 'mlf.jpg'
    }
]

contact_info = {
    'email': 'example.email@example.com',
    'phone': '+353 (555) 123-4567',
    'location': 'Dublin City, Ireland',
    'linkedin': 'https://linkedin.com/in/example',
    'github': 'https://github.com/example'
}

@app.route('/')
def home():
    """Home page route"""
    return render_template('home.html', projects=projects_data[:2])

@app.route('/projects')
def projects():
    """Projects page route"""
    return render_template('projects.html', projects=projects_data)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    """Individual project detail page"""
    project = next((p for p in projects_data if p['id'] == project_id), None)
    if project:
        return render_template('project_detail.html', project=project)
    return redirect(url_for('projects'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route handling both GET and POST requests"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        if name and email and message:
            # In a real application, you would save this to a database or send an email
            flash(f'Thank you {name}! Your message has been sent successfully.', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html', contact_info=contact_info)

if __name__ == '__main__':
    app.run(debug=True)