module.exports = {
  apps: [{
    name: 'magmarine-backend',
    script: './start.sh',
    cwd: '/var/www/magmarine/backend',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G'
  }]
}
