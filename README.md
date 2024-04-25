# Turtle Challenge

This is a judge service for SITCON Camp 2024. We have some problem based on turtle python package. 

## How to build docker container and run
```
docker build -t turtle_judge . # Build the docker
docker images # verify the image
docker run -it --rm turtle_judge # go to docker env
```

## How to use this it
### Play with Turtle
- All python script should be put in `src/`. You can play with Turtle screen, and see the result on your host machine. 
### Implement your turtle algorithm
- Complete `drawing()` function in `example_turtle_script.py`
### Judge service
1. Ak collected python script on judge website(Not yet)
2. Transfer python script to host machine.
3. Run `./judge.sh <python_script.py> <output_png_filename>` at local. This judge will take your implement result png file in `./result` and compared to solution png file in './solution'. And it outputs the similarity percentage based on pixel.
4. Return similarity percentage as score, send back to judge website.

## TODO
- Write a judge script in `./judge_service`. 
- Think about problem and wirte the solution script in `./judge_service/solution_script` 
- Put `./judge.sh` `./solution` `./solution_script` into `.gitignore` after finish development 
- Implement png file similarity test in `./judge.sh`
- Set the score baselin
  - e.g: 
    - 0 ~ 25: 2 points
    - 26 ~ 50: 3 points
    - 51 ~ 75: 4 points
    - 76 ~ 100: 5 points  
## Note
- Check with judging web service with @AK