# Xen

Role to setup xen servers.

# Variables
## Server

Note: More options can be seen in `defaults/main.yml`

- `xen_enable_domains_save`: Enable Xen domain save feature. Default `true`
- `xen_sched_credit_domains`: Set custom domain scheduling credits - persistent over restart. Default `[]`
- `xen_sched_credit_domains_apply`: Apply the domain scheduling during ansible run. Default `false`

Example
```YAML
xen_sched_credit_domains:
    - name: Domain-0
      weight: 512
```

# License
MIT
