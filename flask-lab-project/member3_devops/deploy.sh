#!/bin/bash

# Deployment Scripts - Member 3 (DevOps Engineer)
# Collection of useful deployment and management scripts

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
APP_NAME="flask-lab-project"
DOCKER_IMAGE="flask-lab-project"
PORT=5000

# ============================================
# Utility Functions
# ============================================

print_header() {
    echo -e "${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# ============================================
# Docker Functions
# ============================================

docker_build() {
    print_header "Building Docker Image"
    
    cd main
    
    if docker build -t $DOCKER_IMAGE:latest .; then
        print_success "Docker image built successfully"
        
        # Show image details
        docker images $DOCKER_IMAGE:latest
    else
        print_error "Docker build failed"
        exit 1
    fi
    
    cd ..
}

docker_run() {
    print_header "Running Docker Container"
    
    # Check if container already exists
    if docker ps -a --format '{{.Names}}' | grep -q "^${APP_NAME}$"; then
        print_warning "Container exists. Stopping and removing..."
        docker stop $APP_NAME 2>/dev/null || true
        docker rm $APP_NAME 2>/dev/null || true
    fi
    
    # Run container
    docker run -d \
        --name $APP_NAME \
        -p $PORT:5000 \
        --restart unless-stopped \
        --health-cmd="curl -f http://localhost:5000/health || exit 1" \
        --health-interval=30s \
        --health-timeout=3s \
        --health-retries=3 \
        $DOCKER_IMAGE:latest
    
    print_success "Container started successfully"
    
    # Wait for health check
    print_warning "Waiting for application to be healthy..."
    sleep 5
    
    if docker ps --filter "name=$APP_NAME" --filter "health=healthy" | grep -q $APP_NAME; then
        print_success "Application is healthy!"
        echo -e "\n${GREEN}Access the application at: http://localhost:$PORT${NC}\n"
    else
        print_warning "Application is starting up..."
        echo "Check status with: docker ps"
    fi
}

docker_stop() {
    print_header "Stopping Docker Container"
    
    if docker ps --format '{{.Names}}' | grep -q "^${APP_NAME}$"; then
        docker stop $APP_NAME
        docker rm $APP_NAME
        print_success "Container stopped and removed"
    else
        print_warning "Container not running"
    fi
}

docker_logs() {
    print_header "Container Logs"
    docker logs -f $APP_NAME
}

docker_shell() {
    print_header "Opening Shell in Container"
    docker exec -it $APP_NAME /bin/bash
}

docker_stats() {
    print_header "Container Statistics"
    docker stats $APP_NAME
}

# ============================================
# Testing Functions
# ============================================

run_tests() {
    print_header "Running Unit Tests"
    
    cd main
    
    if [ ! -d "venv" ]; then
        print_warning "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    source venv/bin/activate
    pip install -q -r requirements.txt
    
    pytest tests/ -v --cov=. --cov-report=term-missing
    
    deactivate
    cd ..
}

run_integration_tests() {
    print_header "Running Integration Tests"
    
    # Start container if not running
    if ! docker ps --format '{{.Names}}' | grep -q "^${APP_NAME}$"; then
        print_warning "Starting container for testing..."
        docker_run
        sleep 10
    fi
    
    # Test endpoints
    echo "Testing endpoints..."
    
    # Test health
    if curl -f http://localhost:$PORT/health >/dev/null 2>&1; then
        print_success "Health check passed"
    else
        print_error "Health check failed"
        return 1
    fi
    
    # Test homepage
    if curl -f http://localhost:$PORT/ >/dev/null 2>&1; then
        print_success "Homepage test passed"
    else
        print_error "Homepage test failed"
        return 1
    fi
    
    # Test API
    if curl -f http://localhost:$PORT/api/info >/dev/null 2>&1; then
        print_success "API info test passed"
    else
        print_error "API info test failed"
        return 1
    fi
    
    # Test POST endpoint
    response=$(curl -X POST http://localhost:$PORT/data \
        -H "Content-Type: application/json" \
        -d '{"name":"Test","message":"Integration test"}' \
        -w "%{http_code}" -o /dev/null -s)
    
    if [ "$response" = "201" ]; then
        print_success "POST endpoint test passed"
    else
        print_error "POST endpoint test failed (status: $response)"
        return 1
    fi
    
    print_success "All integration tests passed!"
}

load_test() {
    print_header "Running Load Test"
    
    # Check if ab (Apache Bench) is installed
    if ! command -v ab &> /dev/null; then
        print_error "Apache Bench not installed. Install with: apt-get install apache2-utils"
        return 1
    fi
    
    # Ensure app is running
    if ! docker ps --format '{{.Names}}' | grep -q "^${APP_NAME}$"; then
        print_error "Application not running. Start it first."
        return 1
    fi
    
    echo "Running load test: 1000 requests, 10 concurrent..."
    ab -n 1000 -c 10 http://localhost:$PORT/
}

# ============================================
# Deployment Functions
# ============================================

deploy_local() {
    print_header "Local Deployment"
    
    docker_build
    docker_stop
    docker_run
    
    print_success "Local deployment complete!"
}

deploy_production() {
    print_header "Production Deployment (Simulation)"
    
    print_warning "This is a simulation. Implement your actual deployment here."
    
    # Steps for production deployment:
    echo "1. Run tests"
    run_tests || exit 1
    
    echo "2. Build Docker image"
    docker_build
    
    echo "3. Tag image for registry"
    docker tag $DOCKER_IMAGE:latest $DOCKER_IMAGE:v$(date +%Y%m%d-%H%M%S)
    
    echo "4. Push to registry (commented out)"
    # docker push $DOCKER_IMAGE:latest
    # docker push $DOCKER_IMAGE:v$(date +%Y%m%d-%H%M%S)
    
    echo "5. Deploy to server (commented out)"
    # ssh user@production-server "docker pull $DOCKER_IMAGE:latest && docker-compose up -d"
    
    print_success "Production deployment steps completed"
}

# ============================================
# Monitoring Functions
# ============================================

health_check() {
    print_header "Health Check"
    
    if curl -f http://localhost:$PORT/health 2>/dev/null; then
        print_success "Application is healthy"
    else
        print_error "Application is not responding"
        return 1
    fi
}

monitor() {
    print_header "Monitoring Dashboard"
    
    while true; do
        clear
        echo -e "${BLUE}Flask Lab Project - Monitoring${NC}"
        echo "================================"
        echo ""
        
        # Container status
        echo -e "${YELLOW}Container Status:${NC}"
        docker ps --filter "name=$APP_NAME" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
        echo ""
        
        # Health check
        echo -e "${YELLOW}Health Status:${NC}"
        health_check 2>/dev/null && echo -e "${GREEN}Healthy${NC}" || echo -e "${RED}Unhealthy${NC}"
        echo ""
        
        # Resource usage
        echo -e "${YELLOW}Resource Usage:${NC}"
        docker stats $APP_NAME --no-stream --format "table {{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}" 2>/dev/null || echo "Container not running"
        echo ""
        
        echo "Press Ctrl+C to exit"
        sleep 5
    done
}

# ============================================
# Maintenance Functions
# ============================================

cleanup() {
    print_header "Cleanup"
    
    # Remove stopped containers
    echo "Removing stopped containers..."
    docker container prune -f
    
    # Remove unused images
    echo "Removing unused images..."
    docker image prune -f
    
    # Remove unused volumes
    echo "Removing unused volumes..."
    docker volume prune -f
    
    # Remove unused networks
    echo "Removing unused networks..."
    docker network prune -f
    
    print_success "Cleanup complete"
}

backup() {
    print_header "Backup"
    
    BACKUP_DIR="backups"
    TIMESTAMP=$(date +%Y%m%d-%H%M%S)
    
    mkdir -p $BACKUP_DIR
    
    # Backup Docker image
    echo "Backing up Docker image..."
    docker save $DOCKER_IMAGE:latest | gzip > $BACKUP_DIR/${DOCKER_IMAGE}-${TIMESTAMP}.tar.gz
    
    print_success "Backup saved to $BACKUP_DIR/${DOCKER_IMAGE}-${TIMESTAMP}.tar.gz"
}

# ============================================
# Main Menu
# ============================================

show_menu() {
    clear
    print_header "Flask Lab Project - DevOps Tools"
    echo ""
    echo "Docker Commands:"
    echo "  1) Build Docker image"
    echo "  2) Run Docker container"
    echo "  3) Stop Docker container"
    echo "  4) View logs"
    echo "  5) Open shell in container"
    echo "  6) View container stats"
    echo ""
    echo "Testing:"
    echo "  7) Run unit tests"
    echo "  8) Run integration tests"
    echo "  9) Run load test"
    echo ""
    echo "Deployment:"
    echo "  10) Deploy locally"
    echo "  11) Deploy to production (simulation)"
    echo ""
    echo "Monitoring:"
    echo "  12) Health check"
    echo "  13) Monitor (live dashboard)"
    echo ""
    echo "Maintenance:"
    echo "  14) Cleanup Docker resources"
    echo "  15) Backup Docker image"
    echo ""
    echo "  0) Exit"
    echo ""
    read -p "Enter your choice: " choice
    
    case $choice in
        1) docker_build ;;
        2) docker_run ;;
        3) docker_stop ;;
        4) docker_logs ;;
        5) docker_shell ;;
        6) docker_stats ;;
        7) run_tests ;;
        8) run_integration_tests ;;
        9) load_test ;;
        10) deploy_local ;;
        11) deploy_production ;;
        12) health_check ;;
        13) monitor ;;
        14) cleanup ;;
        15) backup ;;
        0) exit 0 ;;
        *) print_error "Invalid choice" ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
    show_menu
}

# ============================================
# Script Entry Point
# ============================================

# Check if running with arguments
if [ $# -eq 0 ]; then
    show_menu
else
    case $1 in
        build) docker_build ;;
        run) docker_run ;;
        stop) docker_stop ;;
        logs) docker_logs ;;
        test) run_tests ;;
        integration-test) run_integration_tests ;;
        deploy) deploy_local ;;
        health) health_check ;;
        cleanup) cleanup ;;
        backup) backup ;;
        *)
            echo "Usage: $0 [build|run|stop|logs|test|integration-test|deploy|health|cleanup|backup]"
            exit 1
            ;;
    esac
fi
