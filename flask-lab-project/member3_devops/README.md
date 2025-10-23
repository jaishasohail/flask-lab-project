# Member 3 - DevOps Engineer Directory

## Responsibilities
- Create and maintain Dockerfile
- Set up CI/CD pipeline with GitHub Actions
- Configure automated testing
- Manage Docker builds and deployments
- Document deployment procedures

## Work Branch
`devops`

## Tasks Completed
- [ ] Create Dockerfile
- [ ] Create .dockerignore file
- [ ] Set up GitHub Actions workflow
- [ ] Configure automated testing in pipeline
- [ ] Set up Docker Hub integration (optional)
- [ ] Add health checks to Docker container
- [ ] Document deployment process
- [ ] Create docker-compose.yml (optional)

## How to Work
1. Create and checkout your branch:
   ```bash
   git checkout -b devops
   ```

2. Work on Docker and CI/CD files:
   - Dockerfile: `main/Dockerfile`
   - CI/CD: `main/.github/workflows/ci-cd.yml`

3. Test Docker locally:
   ```bash
   cd ../main
   docker build -t flask-lab-project:test .
   docker run -p 5000:5000 flask-lab-project:test
   # Test at http://localhost:5000
   ```

4. Test CI/CD:
   - Push changes to trigger pipeline
   - Monitor GitHub Actions tab

5. Commit and push:
   ```bash
   git add .
   git commit -m "ci: update CI/CD pipeline"
   git push origin devops
   ```

6. Create Pull Request to merge into main

## Docker Commands Reference

### Build Image
```bash
docker build -t flask-lab-project:latest main/
```

### Run Container
```bash
docker run -d -p 5000:5000 --name flask-app flask-lab-project:latest
```

### Stop Container
```bash
docker stop flask-app
docker rm flask-app
```

### View Logs
```bash
docker logs flask-app
```

### Execute Commands in Container
```bash
docker exec -it flask-app /bin/bash
```

## CI/CD Pipeline Overview

The pipeline runs on every push to main and includes:
1. **Test Job**: Runs pytest with coverage
2. **Build Job**: Builds Docker image and tests it
3. **Docker Hub Push**: (Optional) Pushes to Docker Hub
4. **Summary**: Generates deployment summary

## Notes
- Ensure Dockerfile uses best practices
- Keep images small and secure
- Use multi-stage builds if needed
- Configure proper health checks
- Document all environment variables
- Set up secrets in GitHub for Docker Hub
