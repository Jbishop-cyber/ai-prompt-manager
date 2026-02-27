# Deployment Instructions for Free Platforms

## Overview
This document outlines the deployment instructions for the AI Prompt Manager application on various free hosting platforms.

## Platforms Supported
1. **Heroku**
2. **Vercel**
3. **Glitch**
4. **Railway**

## Heroku Deployment
### Prerequisites
- Install the Heroku CLI.
- Create a Heroku account at [heroku.com](https://www.heroku.com).

### Steps
1. Clone your repository:
   ```bash
   git clone https://github.com/Jbishop-cyber/ai-prompt-manager.git
   cd ai-prompt-manager
   ```
2. Log in to Heroku:
   ```bash
   heroku login
   ```
3. Create a new Heroku application:
   ```bash
   heroku create your-app-name
   ```
4. Deploy your code:
   ```bash
   git push heroku main
   ```
5. Open your application:
   ```bash
   heroku open
   ```

## Vercel Deployment
### Prerequisites
- Create an account at [vercel.com](https://vercel.com).

### Steps
1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```
2. In your project directory, run:
   ```bash
   vercel
   ```
3. Follow the prompts to deploy your application.

## Glitch Deployment
### Steps
1. Go to [glitch.com](https://glitch.com) and create a new project.
2. Import from GitHub by entering the repository URL.
3. Glitch will automatically set up your project.
4. You can view your live application at the project URL.

## Railway Deployment
### Steps
1. Go to [railway.app](https://railway.app) and log in.
2. Click on "New Project" and select "Deploy from GitHub".
3. Select your repository and click "Deploy".
4. Your project will be live shortly after deployment.

---

For more advanced deployment options or custom integrations, refer to each platform's official documentation.