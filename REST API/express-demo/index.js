const Joi = require('Joi');
const express = require('express');
const app = express();

app.use(express.json());

const courses = [
    {'id': 1 , 'name': 'course1'},
    {'id': 2 , 'name': 'course2'},
    {'id': 3 , 'name': 'course3'},    
]

app.get('/',(req,res) => {
    res.send('hell>>sjdfnsdnf>>o world');
});

app.get('/api/courses',(req,res) => {
    res.send(courses);

});

app.post('/api/courses/',(req,res) => {

    const schema = {
        name : Joi.string().min(3).required()
    };

    const result = Joi.valid(req.body,schema);
    console.log(result);

       if (!req.body.name || req.body.name.length < 3) {
        // 404 Bad Request
        res.status(400).send('name is required and should be not less than 3');
        return;
    }

    const course = {
        id: courses.length + 1,
        name: req.body.name
    };
    courses.push(course);
    res.send(course);
})

app.get('/api/courses/:id',(req,res) => {
    const course = courses.find(c => c.id === parseInt(req.params.id));
    if (!course) res.status(404).send('the course with the given id not found');
    res.send(course);
});

app.put('/api/courses/:id',(req,res) => {
    const course = courses.find(c => c.id === parseInt(req.params.id));
    if (!course) res.status(404).send('the course with the given id not found');
    
     const result = ValidateCourse(req.body);
     //const {} = ValidateCourse(req.body);
    
    course.name = req.body.name; 
    res.send(course); 
});

// PORT  

function ValidateCourse(course) {
    const schema = {
        name : Joi.string().min(3).required()
    };

    return Joi.valid(course,schema);

};


app.delete('/api/courses/:id', (req,res) => {
    const course = courses.find(c => c.id === parseInt(req.params.id));
    if (!course) return res.status(404).send('the course with the given id not found');
    
    const index = courses.indexOf(course);
    courses.splice(index , 1);

    res.send(courses);
})

const port = process.env.PORT || 3000;
app.listen(port,() => console.log(`listening on port ${port}...`));
