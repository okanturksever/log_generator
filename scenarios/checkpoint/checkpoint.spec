{
    "fields" : [
        { "templateCount" : {"count":6} },
        { "url" : {"type": "from_list_file", "file" : "url.list", "method":"sequential" } },
        { "date": {"type": "random", "generate_type":"datetime", "format": "%d%b%Y %H:%M:%S" } },
        { "ip" : {"type": "from_list_file", "file" : "ip.list", "method":"random" } },
        { "port" : {"type": "random", "generate_type":"integer", "min":1, "max":10000 } }
    ],
    "template" : [
          "loc=780573|filename=fw.log|fileid=1358459940|time=${date}|action=allow|orig=${ip}|orig_name=fw1|i/f_dir=outbound|i/f_name=eth2|has_accounting=0|product=URL Filtering|__policy_id_tag=product=VPN-1 & FireWall-1[db_tag={00000052-0040-004B-86F9-0BC8ACA9E733};mgmt=fw1;date=1357897393;policy_name=Standard]|user=Name Surname (name@domain.local)/n|src_user_name=Name Surname (name@domain.local)/n|src_machine_name=box@domain.local|snid=d283b405|src=${ip}|s_port=${port}|dst=${ip}|service=80|service_name=http|proto=tcp|appi_name=*** Confidential ***|app_desc=*** Confidential ***|app_id=-1093427800|app_category=*** Confidential ***|matched_category=*** Confidential ***|app_properties=*** Confidential ***|app_risk=*** Confidential ***|app_rule_id=*** Confidential ***|app_rule_name=*** Confidential ***|proxy_src_ip=10.1.4.103|bytes=40821|sent_bytes=3366|received_bytes=37455|Suppressed logs=54|Referrer_self_uid=*** Confidential ***|ICMP Code=hede|ICMP Type=hayda|TCP packet out of state=heyoo",
          "loc=477|filename=fw.adtlog|fileid=-1|time=${date}|action=accept|orig=${ip}|orig_name=cpmodule|i/f_dir=outbound|i/f_name=|has_accounting=0|product=SmartDashboard|ObjectName=cpmodule|ObjectType=firewall_application|ObjectTable=applications|Operation=Install Policy|Uid={000000FF-00C2-004D-B087-1E87F2B35AB9}|Administrator=admin|Machine=TestXp|Subject=Policy Installation|Audit Status=Success|Additional Info=Security Policy : Standard|Operation Number=7|client_ip=${ip}",
          "loc=780597|filename=fw.log|fileid=1358459940|time=${date}|action=block|orig=${ip}|orig_name=ch_machine|i/f_dir=outbound|i/f_name=eth2|has_accounting=0|product=Application Control|__policy_id_tag=product=VPN-1 & FireWall-1[db_tag={00000052-0040-004B-86F9-0BC8ACA9E733};mgmt=ch_machine;date=1357897393;policy_name=Standard]|user=ch_user (ch_user@userdomain.local)/n|src_user_name=ch_user (ch_user@userdomain.local)/n|src_machine_name=ch_machine@userdomain.local|snid=895f02c7|src=${ip}|s_port=${port}|dst=${ip}|service=80|service_name=http|proto=tcp|appi_name=*** Confidential ***|app_desc=*** Confidential ***|app_id=60340655|app_category=*** Confidential ***|matched_category=*** Confidential ***|app_properties=*** Confidential ***|app_risk=*** Confidential ***|app_rule_id=*** Confidential ***|app_rule_name=*** Confidential ***|web_client_type=Microsoft IE|proxy_src_ip=${ip}|app_sig_id=60340655:1|UserCheck_incident_uid=A1B97AB1-6D72-6F67-6F76-696EDBB27D75|resource=${url}|UserCheck=*** Confidential ***|user_status=*** Confidential ***|portal_message=*** Confidential ***|UserCheck_Confirmation_Level=Application|frequency=1 days |UserCheck_Interaction_name=*** Confidential ***",
          "loc=780738|filename=fw.log|fileid=1358459940|time=${date}|action=accept|orig=${ip}|orig_name=ch_machine|i/f_dir=inbound|i/f_name=eth2|has_accounting=0|product=VPN-1 & FireWall-1|__policy_id_tag=product=VPN-1 & FireWall-1[db_tag={00000052-0040-004B-86F9-0BC8ACA9E733};mgmt=ch_machine;date=1357897393;policy_name=Standard]|user=jack johns (jackj@userdomain.local)/n|src_user_name=jack johns (jackj@userdomain.local)/n|src_machine_name=jackj@userdomain.local|snid=2c5930e8|inzone=Internal|outzone=External|rule=8|rule_uid={B9F541FB-BF71-4EA5-9B69-3042908E8BF2}|service_id=http|src=${ip}|s_port=${port}|dst=${ip}|service=80|service_name=http|proto=tcp|xlatesrc=${ip}|xlatesport=${port}|xlatedport=0|xlatedport_name=Unknown|NAT_rulenum=8|NAT_addtnl_rulenum=1",
          "loc=13043|filename=fw.log|fileid=1424037540|time=${date}|action=decrypt|orig=${ip}|orig_name=MERKEZFW|i/f_dir=inbound|i/f_name=eth7|has_accounting=0|product=VPN-1 & FireWall-1|inzone=External|outzone=Internal|rule=30|rule_uid={6F0D202D-5115-4C5C-83A5-184DD624122A}|src=${ip}|s_port=${port}|dst=${ip}|service=4163|proto=udp|scheme:=IKE|methods:=ESP: 3DES + SHA1 + PFS (group 2)|peer gateway=212.156.136.34|peer gateway_name=DISASTER_SITE_GW|community=JUNIPER_COMMUNITY|fw_subproduct=VPN-1|vpn_feature_name=VPN|__policy_id_tag=product=VPN-1 & FireWall-1[db_tag={0C1294E2-480E-F54D-864C-CD30EEF243EC};mgmt=gw-37559c;date=1424036478;policy_name=Standard]|origin_sic_name=CN=MERKEZFW,O=gw-37559c.domain.com.tr.nqf27e",
          "loc=13041|filename=fw.log|fileid=1424037540|time=${date}|action=drop|orig=${ip}|orig_name=MERKEZFW|i/f_dir=inbound|i/f_name=eth1|has_accounting=0|product=VPN-1 & FireWall-1|Log ID=404830|inzone=Internal|outzone=External|rule=31|rule_uid={E2F427E8-AC81-4705-B7BB-DA4FAD6540EC}|service_id=icmp-proto|ICMP=Echo Request|src=${ip}|dst=${ip}|proto=icmp|ICMP Type=8|ICMP Code=0|encryption fail reason:=Packet is dropped because there is no valid SA - please refer to solution sk19423 in SecureKnowledge Database for more information|scheme:=IKE|methods:=ESP: DES + SHA1|peer gateway=${ip}|peer gateway_name=MERKEZ_GW|community=ZyXEL_COMMUNITY|fw_subproduct=VPN-1|vpn_feature_name=VPN|src_machine_name=monitoringsrv@domain.int|snid=266de7e9|__policy_id_tag=product=VPN-1 & FireWall-1[db_tag={0C1294E2-480E-F54D-864C-CD30EEF243EC};mgmt=gw-37559c;date=1424036478;policy_name=Standard]|origin_sic_name=CN=MERKEZFW,O=gw-37559c.domain.com.tr.nqf27e"
    ]
}