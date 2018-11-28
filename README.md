# Stargazing

Github's repositories stars observer.

This simple script allow to fetch stargazer information of a Github repository.



Run:
```bash
python stargazing.py --acces_token <your_access_token> --repository <repository_name>
```

This would generate a .csv (`<repository_name>-stargazers.csv`) file with all the repository stargazer information.

## Access token
Fetch your access token from [here](https://github.com/settings/tokens)  (https://github.com/settings/tokens)


## Repository name
The repository name should be expressed in the form
profile/repostory. For example, if you wanted to fetch the stargazer of this repository (a gazillion, soon!) that would be `mattiaongit/stargazing`

## Additional cofiguration

Additional configuration are possible via the
- `confing.json` file

Here you could setup

- Stargazer field to fetch*
- Output file name
*
By default the following fields are fetched:
```python
["id", "username", "name", "email", "location", "company", "followers", "following","public_repos", "created_at",
 "star_time", "url"]
```
