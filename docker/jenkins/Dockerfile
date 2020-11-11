FROM jenkins/inbound-agent

LABEL maintainer="Mikhail Gr"
LABEL description="You can build image with Jenkins agent, NodeJS and Newman from this Dockerfile"

ARG user=jenkins

USER root

RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
 && apt-get install -y nodejs \
 && curl -L https://www.npmjs.com/install.sh | sh \
 && npm install -g newman \
 && apt-get autoclean -y \
 && apt-get autoremove -y

USER ${user}

ENTRYPOINT ["java", "-jar", "/usr/share/jenkins/agent.jar"]

#------------------------------------------
# Run Jenkins master in docker container:
# docker run -i --rm --name jenkins_master -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
#
# Run Jenkins agent in docker container:
# docker build -t jenkins_agent_nodejs .
# docker run -i --rm --name agent1 -v agent1-workdir:/home/jenkins/agent jenkins_agent_nodejs -jnlpUrl ${jnlp_path} -secret ${secret_key} -workDir /home/jenkins/agent