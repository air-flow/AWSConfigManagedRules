### access-keys-rotated

>アクティブなアクセスキーが、maxAccessKeyAge で指定された日数内にローテーションされるかどうかを確認します。アクセスキーが最大日数の maxAccessKeyAge を超えても更新されていない場合、ルールは NON_COMPLIANT です。
>[access-keys-rotated](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/access-keys-rotated.html)

### account-part-of-organizations

>AWS アカウントが AWS Organizations の一部であるかどうかを確認します。AWS アカウントが AWS Organizations の一部ではない場合、または AWS Organizations のマスターアカウント ID がルールパラメータ MasterAccountId と一致しない場合は、ルールは NON_COMPLIANT です。
>[account-part-of-organizations](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/account-part-of-organizations.html)

### acm-certificate-expiration-check

>アカウントの AWS Certificate Manager 証明書が、指定の日数以内で有効期限切れとしてマークされているかどうかを確認します。ACM が提供する証明書は自動的に更新されます。ACM は、ユーザーがインポートした証明書を自動的に更新しません。証明書の有効期限が近づいている場合、ルールは NON_COMPLIANT です。
>[acm-certificate-expiration-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/acm-certificate-expiration-check.html)

### alb-http-drop-invalid-header-enabled

>AWS Application Load Balancers (ALB) が http ヘッダーをドロップするように設定されていることをルールが評価するかどうかを確認します。routing.http.drop_invalid_header_fields.enabled の値が false に設定されている場合、ルールは NON_COMPLIANT です。
>[alb-http-drop-invalid-header-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/alb-http-drop-invalid-header-enabled.html)

### alb-http-to-https-redirection-check

>HTTP から HTTPS へのリダイレクトが Application Load Balancer のすべての HTTP リスナーで設定されているかどうかを確認します。Application Load Balancer の 1 つまたは複数の HTTP リスナーに HTTP から HTTPS へのリダイレクトが設定されていない場合、ルールは NON_COMPLIANT です。また、1 つ以上の HTTP リスナーが、リダイレクトではなく HTTP リスナーへの転送を行っている場合、ルールは NON_COMPLIANT となります。
>[alb-http-to-https-redirection-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/alb-http-to-https-redirection-check.html)

### alb-waf-enabled

>Application Load Balancer (ALB) でウェブアプリケーションファイアウォール (WAF) が有効になっているかどうかを確認します。key: waf.enabled が false に設定されている場合、このルールは NON_COMPLIANT です。
>[alb-waf-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/alb-waf-enabled.html)

### api-gw-associated-with-waf

>Amazon API Gateway API ステージで AWS WAF ウェブ ACL が使用されているかどうかを確認します。AWS WAF ウェブ ACL が使用されていないか、または使用されている AWS ウェブ ACL が、ルールパラメータにリストされているものと一致しない場合、このルールは NON_COMPLIANT です。
>[api-gw-associated-with-waf](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/api-gw-associated-with-waf.html)

### api-gw-cache-enabled-and-encrypted

>Amazon API Gateway ステージのすべてのメソッドでキャッシュが有効になっているか、および暗号化されているかどうかを確認します。Amazon API Gateway ステージのいずれかのメソッドでキャッシュが設定されていない場合、またはキャッシュが暗号化されていない場合、ルールは NON_COMPLIANT です。
>[api-gw-cache-enabled-and-encrypted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/api-gw-cache-enabled-and-encrypted.html)

### api-gw-endpoint-type-check

>Amazon API Gateway の API がルールパラメータ endpointConfigurationType で指定されたタイプであることを確認します。REST API がルールパラメータで設定されたエンドポイントタイプと一致しない場合、ルールは NON_COMPLIANT を返します。
>[api-gw-endpoint-type-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/api-gw-endpoint-type-check.html)

### api-gw-execution-logging-enabled

>Amazon API Gateway ステージのすべてのメソッドのログ記録が有効になっていることを確認します。ログ記録が有効でない場合、ルールは NON_COMPLIANT です。loggingLevel が ERROR でも INFO でもない場合、ルールは NON_COMPLIANT です。
>[api-gw-execution-logging-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/api-gw-execution-logging-enabled.html)

### api-gw-ssl-enabled

>REST API ステージで Secure Sockets Layer (SSL) 証明書が使用されるかどうかを確認します。REST API ステージに関連する SSL 証明書がない場合、このルールは NON_COMPLIANT です。
>[api-gw-ssl-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/api-gw-ssl-enabled.html)

### api-gw-xray-enabled

>Amazon API Gateway REST API で AWS X-Ray トレースが有効になっているかどうかを確認します。X-Ray トレースが有効になっている場合、このルールは COMPLIANT です。そうでない場合は、NON_COMPLIANT です。
>[api-gw-xray-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/api-gw-xray-enabled.html)

### approved-amis-by-id

>実行中のインスタンスで指定された AMI が使用されているかどうかを確認します。承認済み AMI ID のリストを指定します。実行中のインスタンスで使用されている AMI が、このリストにない場合は NON_COMPLIANT です。
>[approved-amis-by-id](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/approved-amis-by-id.html)

### approved-amis-by-tag

>実行中のインスタンスで指定された AMI が使用されているかどうかを確認します。AMI を識別するタグを指定します。実行中のインスタンスで使用されている AMI に、指定したタグの少なくとも 1 つがない場合は NON_COMPLIANT です。
>[approved-amis-by-tag](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/approved-amis-by-tag.html)

### aurora-mysql-backtracking-enabled

>Amazon Aurora MySQL クラスターでバックトラッキングが有効になっているかどうかを確認します。Aurora クラスターで MySQL が使用されているが、バックトラッキングが有効になっていない場合、このルールは NON_COMPLIANT です。
>[aurora-mysql-backtracking-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/aurora-mysql-backtracking-enabled.html)

### バックアップ計画によって保護された Aurora リソース

>Amazon Aurora DB クラスターがバックアッププランで保護されているかどうかを確認します。Amazon Relational Database Service (Amazon RDS) データベースクラスターがバックアッププランによって保護されていない場合、ルールは NON_COMPLIANT です。
>[バックアップ計画によって保護された Aurora リソース](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/aurora-resources-protected-by-backup-plan.html)

### autoscaling-group-elb-healthcheck-required

>ロードバランサーに関連付けられた Auto Scaling グループで、Elastic Load Balancing のヘルスチェックが使用されているかどうかを確認します。
>[autoscaling-group-elb-healthcheck-required](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/autoscaling-group-elb-healthcheck-required.html)

### autoscaling-launch-config-public-ip-disabled

>Amazon EC2 Auto Scaling グループのパブリック IP アドレスが、起動設定によって有効になっているかどうかを確認します。Auto Scaling グループの起動設定で、AssociatePublicIpAddress が「true」に設定されている場合、このルールは NON_COMPLIANT です。
>[autoscaling-launch-config-public-ip-disabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/autoscaling-launch-config-public-ip-disabled.html)

### autoscaling-multiple-az

>Auto Scaling グループが複数のアベイラビリティーゾーンにまたがっているかどうかを確認します。Auto Scaling グループが複数のアベイラビリティーゾーンにまたがっていない場合、ルールは NON_COMPLIANT になります。
>[autoscaling-multiple-az](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/autoscaling-multiple-az.html)

### バックアップ計画-分-頻度と分保持チェック

>バックアッププランに、必要な頻度と保存期間を満たすバックアップルールがあるかどうかを確認します。このルールは、少なくとも指定した頻度と同じ頻度でリカバリポイントが作成されない場合、または指定した期間より前に期限切れになる場合は、非準拠です。
>[バックアップ計画-分-頻度と分保持チェック](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/backup-plan-min-frequency-and-min-retention-check.html)

### バックアップ/リカバリポイント暗号化

>リカバリポイントが暗号化されているかどうかを確認します。リカバリポイントが暗号化されていない場合、ルールは NON_COMPLIANT です。
>[バックアップ/リカバリポイント暗号化](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/backup-recovery-point-encrypted.html)

### バックアップ/リカバリポイントの手動削除/無効化

>バックアップボールトに、リカバリポイントの削除を防ぐリソースベースのポリシーが添付されているかどうかを確認します。バックアップボールトにリソースベースのポリシーがない場合、または適切な「拒否」ステートメントのないポリシーがある場合、ルールは NON_COMPLIANT です。
>[バックアップ/リカバリポイントの手動削除/無効化](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/backup-recovery-point-manual-deletion-disabled.html)

### バックアップ/リカバリポイントの最小保存期間チェック

>リカバリポイントが、指定した期間より前に期限切れになるかどうかを確認します。リカバリポイントに必要な保持期間より短いリテンションポイントがある場合、ルールは NON_COMPLIANT です。
>[バックアップ/リカバリポイントの最小保存期間チェック](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/backup-recovery-point-minimum-retention-check.html)

### beanstalk-enhanced-health-reporting-enabled

>AWS Elastic Beanstalk 環境が拡張ヘルスレポートを作成するよう設定されているかどうかを確認します。この環境が拡張ヘルスレポートを作成するよう設定されている場合、ルールは COMPLIANT です。環境が基本ヘルスレポートを作成するよう設定されている場合、ルールは NON_COMPLIANT です。
>[beanstalk-enhanced-health-reporting-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/beanstalk-enhanced-health-reporting-enabled.html)

### clb-multiple-az

>Classic Load Balancer が複数のアベイラビリティーゾーン (AZ) にまたがるかどうかをチェックします。Classic Load Balancer が 2 AZ 未満の場合、または minAvailabilityZones パラメータ (指定されている場合) に記載されている数の AZ にまたがっていない場合は、ルールは NON_COMPLIANT です。
>[clb-multiple-az](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/clb-multiple-az.html)

### cloudformation-stack-drift-detection-check

>Cloud Formation スタックの実際の設定が、意図した設定と異なっているかどうか、またはドリフトしているかどうかを確認します。スタックの 1 つ以上のリソースが意図した設定と異なっている場合、スタックはドリフトしたと見なされます。このルールとスタックは、スタックのドリフトステータスが IN_SYNC の場合、COMPLIANT です。このルールとスタックは、スタックのドリフトステータスが DRIFTED の場合、NON_COMPLIANT です。
>[cloudformation-stack-drift-detection-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudformation-stack-drift-detection-check.html)

### cloudformation-stack-notification-check

>CloudFormation スタックが SNS トピックにイベント通知を送信しているかどうか確認します。オプションで、指定された SNS トピックが使用されているかどうか確認します。
>[cloudformation-stack-notification-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudformation-stack-notification-check.html)

### cloudfront-accesslogs-enabled

>Amazon CloudFront ディストリビューションが、Amazon Simple Storage Service (Amazon S3) サーバーアクセスログから情報をキャプチャするように設定されているかどうかを確認します。CloudFront ディストリビューションにログ記録が設定されていない場合、このルールは NON_COMPLIANT です。
>[cloudfront-accesslogs-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-accesslogs-enabled.html)

### cloudfront-associated-with-waf

>Amazon CloudFront ディストリビューションが WAF または WAFv2 ウェブアクセスコントロールリスト (ACL) に関連付けられているかどうかを確認します。CloudFront ディストリビューションがウェブ ACL に関連付けられていない場合、このルールは NON_COMPLIANT です。
>[cloudfront-associated-with-waf](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-associated-with-waf.html)

### cloudfront-custom-ssl-certificate

>Amazon CloudFront ディストリビューションに関連付けられている証明書が、デフォルトの Secure Sockets Layer (SSL) 証明書であるかどうかを確認します。CloudFront ディストリビューションでデフォルトの SSL 証明書が使用される場合、このルールは NON_COMPLIANT です。
>[cloudfront-custom-ssl-certificate](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-custom-ssl-certificate.html)

### cloudfront-default-root-object-configured

>Amazon CloudFront ディストリビューションが、デフォルトのルートオブジェクトである特定のオブジェクトを返すように設定されているかどうかを確認します。Amazon CloudFront ディストリビューションにデフォルトのルートオブジェクトが設定されていない場合、ルールは NON_COMPLIANT です。
>[cloudfront-default-root-object-configured](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-default-root-object-configured.html)

### cloudfront-no-deprecated-ssl-protocols

>CloudFront ディストリビューションが CloudFront エッジロケーションとカスタムオリジン間の HTTPS 通信に非推奨の SSL プロトコルを使用しているかどうかを確認します。「OriginSslProtocols」に「SSLv3」が含まれる場合、このルールは CloudFront ディストリビューションでは非準拠です。
>[cloudfront-no-deprecated-ssl-protocols](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-no-deprecated-ssl-protocols.html)

### cloudfront-origin-access-identity-enabled

>S3 オリジンタイプの Amazon CloudFront ディストリビューションにオリジンアクセスアイデンティティ (OAI) が設定されているかどうかを確認します。CloudFront ディストリビューションが S3 によってバックアップされていて、いずれかの S3 オリジンタイプが OAI 設定されていない場合、ルールは NON_COMPLIANT です。オリジンが S3 バケットでない場合、ルールは NON_COMPLIANT です。オリジンが S3 バケットではない場合、ルールは NOT_APPLICABLE を返しません。
>[cloudfront-origin-access-identity-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-origin-access-identity-enabled.html)

### cloudfront-origin-failover-enabled

>Amazon CloudFront のオリジングループ内の少なくとも 2 つのオリジンのディストリビューションに対してオリジングループが設定されているかどうかを確認します。ディストリビューションのオリジングループがない場合、このルールは NON_COMPLIANT です。
>[cloudfront-origin-failover-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-origin-failover-enabled.html)

### cloudfront-sni-enabled

>Amazon CloudFront ディストリビューションでカスタム SSL 証明書が使用されていて、SNI を使用して HTTPS リクエストを処理するように設定されているかどうかを確認します。カスタム SSL 証明書が関連付けられているものの、SSL サポートメソッドが専用 IP アドレスである場合、このルールは NON_COMPLIANT です。
>[cloudfront-sni-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-sni-enabled.html)

### loudfront-traffic-to-origin-encrypted

>Amazon CloudFront ディストリビューションがカスタムオリジンへのトラフィックを暗号化しているかどうかを確認します。「OriginProtocolPolicy」が「http のみ」の場合、または「OriginProtocolPolicy」が「マッチビューア」で「ViewerProtocolPolicy」が「すべて許可」の場合、ルールは非準拠です。
>[loudfront-traffic-to-origin-encrypted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-traffic-to-origin-encrypted.html)

### cloudfront-viewer-policy-https

>Amazon CloudFront ディストリビューションが HTTPS を (直接またはリダイレクト経由で) 使用しているかどうかを確認します。ViewerProtocolPolicy の値が defaultCacheBehavior または cacheBehaviors に対して 'allow-all' に設定されている場合、ルールは NON_COMPLIANT です。
>[cloudfront-viewer-policy-https](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudfront-viewer-policy-https.html)

### cloudtrail-s3-dataevents-enabled

>少なくとも 1 つの AWS CloudTrail 証跡がすべての S3 バケットの Amazon S3 データイベントをログ記録しているかどうかを確認します。S3 バケットのデータイベントをログに記録する証跡が設定されていない場合、ルールは NON_COMPLIANT です。
>[cloudtrail-s3-dataevents-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudtrail-s3-dataevents-enabled.html)

### cloudtrail-security-trail-enabled

>セキュリティのベストプラクティスを使用して定義された AWS CloudTrail 証跡が少なくとも 1 つあることを確認します。次のすべてを満たす証跡が少なくとも 1 つある場合、このルールは COMPLIANT です:
>[cloudtrail-security-trail-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudtrail-security-trail-enabled.html)

### cloudwatch-alarm-action-check

>CloudWatch アラームで、少なくとも 1 つのアラームアクション、1 つの INSUFFICIENT_DATA アクション、または 1 つの OK アクションが有効になっているかどうかを確認します。必要に応じて、指定した ARN のいずれかに一致するアクションがあるかどうかを確認します。
>[cloudwatch-alarm-action-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudwatch-alarm-action-check.html)

### cloudwatch-alarm-action-enabled-check

>Amazon CloudWatch アラームアクションが有効な状態にあるかどうかをチェックします。CloudWatch アラームアクションが有効状態でない場合、ルールは NON_COMPLIANT です。
>[cloudwatch-alarm-action-enabled-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudwatch-alarm-action-enabled-check.html)

### cloudwatch-alarm-resource-check

>指定したリソースタイプに、指定したメトリクスの CloudWatch アラームがあるかどうかを確認します。リソースタイプとして、EBS ボリューム、EC2 インスタンス、RDS クラスター、または S3 バケットを指定できます。
>[cloudwatch-alarm-resource-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudwatch-alarm-resource-check.html)

### cloudwatch-alarm-settings-check

>特定のメトリクス名を持つ CloudWatch アラームに指定された設定があるかどうかを確認します。
>[cloudwatch-alarm-settings-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudwatch-alarm-settings-check.html)

### cloudwatch-log-group-encrypted

>Amazon CloudWatch Logs のロググループが、AWS Key Management Service (KMS) によって管理されているカスタマーマスターキー (CMK) で暗号化されているかどうかを確認します。AWS KMS CMK がロググループで設定されていない場合、ルールは NON_COMPLIANT です。
>[cloudwatch-log-group-encrypted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudwatch-log-group-encrypted.html)

### cloud-trail-cloud-watch-logs-enabled

>AWS CloudTrail 証跡がログを Amazon CloudWatch Logs に送信するように設定されているかどうかを確認します。証跡の CloudWatchLogsLogGroupArn プロパティが空の場合、この証跡は準拠していません。
>[cloud-trail-cloud-watch-logs-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloud-trail-cloud-watch-logs-enabled.html)

### cloudtrail-enabled

>AWS アカウントで AWS CloudTrail が有効になっているかどうかを確認します。必要に応じて、使用する S3 バケット、SNS トピック、および AWS CloudTrail の ARN を指定できます AWS CloudTrailが有効でない場合、ルールは NON_COMPLIANT です。
>[cloudtrail-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloudtrail-enabled.html)

### cloud-trail-encryption-enabled

>AWS CloudTrail がサーバー側の暗号化 (SSE) AWS Key Management Service KMSキーの暗号化を使用するよう設定されているかどうかを確認します。KmsKeyId が定義されている場合、ルールは COMPLIANT です。
>[cloud-trail-encryption-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloud-trail-encryption-enabled.html)

### cloud-trail-log-file-validation-enabled

>AWS CloudTrail でログを含む署名付きダイジェストファイルが作成されるかどうかを確認します。AWS では、すべての証跡でファイルの検証を有効にすることをお勧めします。検証が有効化されていない場合は、ルールは NON_COMPLIANT です。
>[cloud-trail-log-file-validation-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cloud-trail-log-file-validation-enabled.html)

### cmk-backing-key-rotation-enabled

>各キーのキーローテーションが有効になっていること、およびカスタマーが作成したキー ID AWS KMS key (KMS key) と一致していることを確認します。特定のキーオブジェクトでキーのローテーションが有効になっている場合、ルールは COMPLIANT です。このルールは、インポートされたキーマテリアルを持つ KMS には適用されません。
>[cmk-backing-key-rotation-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cmk-backing-key-rotation-enabled.html)

### codebuild-project-artifact-encryption

>AWS CodeBuild プロジェクトで、そのアーティファクトのすべてに対して暗号化が有効化されているかどうかを確認します。プライマリまたはセカンダリ (存在する場合) のアーティファクト設定のいずれかに「encryptionDisabled」が「true」に設定されていると、ルールは NON_COMPLIANT になります。
>[codebuild-project-artifact-encryption](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codebuild-project-artifact-encryption.html)

### codebuild-project-environment-privileged-check

>AWS CodeBuild プロジェクト環境で特権モードが有効化されているかどうかを確認します。「privilegedMode」が「true」に設定されている場合、ルールは CodeBuild プロジェクトに対して NON_COMPLIANT になります。
>[codebuild-project-environment-privileged-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codebuild-project-environment-privileged-check.html)

### codebuild-project-envvar-awscred-check

>プロジェクトに環境変数 AWS_ACCESS_KEY_ID と AWS_SECRET_ACCESS_KEY が含まれているかどうか確認します。プロジェクト環境変数にプレーンテキストの認証情報が含まれている場合、ルールは NON_COMPLIANT です。
>[codebuild-project-envvar-awscred-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codebuild-project-envvar-awscred-check.html)

### codebuild-project-logging-enabled

>AWS CodeBuild プロジェクト環境で、少なくとも 1 つのログオプションが有効になっているかどうかを確認します。「logsConfig」が存在しない場合、または存在するすべてのログ設定のステータスが「DISABLED」に設定されている場合、ルールは NON_COMPLIANT になります。
>[codebuild-project-logging-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codebuild-project-logging-enabled.html)

### codebuild-project-s3-logs-encrypted

>Amazon S3 ログが設定されている AWS CodeBuild プロジェクトで、そのログに対して暗号化が有効化されているかどうかを確認します。CodeBuild プロジェクトの s3LogsConfig で「encryptionDisabled」が「true」に設定されている場合、ルールは NON_COMPLIANT になります。
>[codebuild-project-s3-logs-encrypted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codebuild-project-s3-logs-encrypted.html)

### codebuild-project-source-repo-url-check

>GitHub または Bitbucket のソースレポジトリの URL に、個人用のアクセストークンまたはユーザー名とパスワードが含まれているかどうか確認します。このルールは、GitHub または Bitbucket レポジトリへのアクセス権限を付与するための OAuth の使用に準拠しています。
>[codebuild-project-source-repo-url-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codebuild-project-source-repo-url-check.html)

### codedeploy-auto-rollback-monitor-enabled

>デプロイグループに、アラームがアタッチされた自動デプロイロールバックとデプロイモニタリングが設定されているかどうかを確認します。AutoRollbackConfiguration もしくは AlarmConfiguration が設定されていない、または有効化されていない場合、ルールは NON_COMPLIANT になります。
>[codedeploy-auto-rollback-monitor-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codedeploy-auto-rollback-monitor-enabled.html)

### codedeploy-ec2-minimum-healthy-hosts-configured

>EC2/オンプレミスコンピューティングプラットフォームのデプロイグループに、正常なホストフリートの最小割合、または入力しきい値以上のホスト数が設定されているかどうかを確認します。どちらかがしきい値を下回っている場合、ルールは NON_COMPLIANT になります。
>[codedeploy-ec2-minimum-healthy-hosts-configured](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codedeploy-ec2-minimum-healthy-hosts-configured.html)

### codedeploy-lambda-allatonce-traffic-shift-disabled

>Lambda コンピューティングプラットフォームのデプロイグループがデフォルトのデプロイ設定を使用していないかどうかを確認します。デプロイグループが「CodeDeployDefault.LambdaAllAtOnce」のデプロイ設定を使用している場合、ルールは NON_COMPLIANT になります。
>[codedeploy-lambda-allatonce-traffic-shift-disabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codedeploy-lambda-allatonce-traffic-shift-disabled.html)

### codepipeline-deployment-count-check

>AWS CodePipeline の最初のデプロイステージで複数のデプロイが実行されるかどうかを確認します。必要に応じて、後続の残りの各ステージで、指定された数 (deploymentLimit) を超えるデプロイが実行されているかどうかを確認します。
>[codepipeline-deployment-count-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codepipeline-deployment-count-check.html)

### codepipeline-region-fanout-check

>AWS CodePipeline の各ステージで、以前のすべてのステージで AWS CodePipeline によってデプロイされたリージョンの数の N 倍を超えるリージョンにデプロイしているかどうかを確認します (N はリージョンファンアウト数)。最初のデプロイステージでは最大 1 個のリージョンにデプロイでき、2 番目のデプロイステージでは regionFanoutFactor で指定された最大数までデプロイできます。regionFanoutFactor を指定しない場合、デフォルト値は 3 です。例えば、最初のデプロイステージで 1 つのリージョンにデプロイし、2 番目のデプロイステージで 3 つのリージョンにデプロイする場合、3 番目のデプロイステージでは 12 のリージョン、つまり、以前のステージの合計数にファンアウトリージョン数 (3) を乗算した数までデプロイできます。ルールは、デプロイ先の数が第 1 ステージで 1 リージョン、2 番目のステージで 3 リージョン、または 3 番目のステージで 12 リージョンを超える場合、ルールは NON_COMPLIANT です。
>[codepipeline-region-fanout-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/codepipeline-region-fanout-check.html)

### cw-loggroup-retention-period-check

>Amazon CloudWatch LogGroup の保持期間が特定の日数に設定されているかどうかを確認します。ロググループの保持期間が MinRetentionTime パラメータより短い場合、ルールは NON_COMPLIANT です。
>[cw-loggroup-retention-period-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/cw-loggroup-retention-period-check.html)

### dax-encryption-enabled

>Amazon DynamoDB Accelerator (DAX) クラスターが暗号化されていることを確認します。DAX クラスターが暗号化されていない場合、ルールは NON_COMPLIANT です
>[dax-encryption-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dax-encryption-enabled.html)

### db-instance-backup-enabled

>RDS DB インスタンスでバックアップが有効になっているかどうかを確認します。オプションで、バックアップ保存期間およびバックアップウィンドウを確認します。
>[db-instance-backup-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/db-instance-backup-enabled.html)

### desired-instance-tenancy

>インスタンスのテナンシーが指定したものかどうかを確認します。AMI からインスタンスが起動されているかどうかを確認するには AMI ID を指定し、専有ホストからインスタンスが起動されているかどうかを確認するにはホスト ID を指定します。複数の ID 値はカンマで区切ります。
>[desired-instance-tenancy](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/desired-instance-tenancy.html)

### desired-instance-type

>EC2 インスタンスのインスタンスタイプが指定したものであるかどうかを確認します。
>[desired-instance-type](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/desired-instance-type.html)

### dms-replication-not-public

>AWS Database Migration Service のレプリケーションインスタンスがパブリックであるかどうかを確認します。PubliclyAccessible フィールドが true の場合、ルールは NON_COMPLIANT です。
>[dms-replication-not-public](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dms-replication-not-public.html)

### dynamodb-autoscaling-enabled

>Auto Scaling またはオンデマンドが DynamoDB テーブル、グローバルセカンダリインデックス、またはその両方で有効になっているかどうかを確認します。必要に応じて、テーブルまたはグローバルセカンダリインデックスの読み取りおよび書き込みキャパシティーユニットを設定できます。
>[dynamodb-autoscaling-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dynamodb-autoscaling-enabled.html)

### dynamodb-in-backup-plan

>Amazon DynamoDB テーブルが AWS Backup プランに存在するかどうかを確認します。Amazon DynamoDB テーブルがどの AWS Backup プランにも存在しない場合、ルールは NON_COMPLIANT です。
>[dynamodb-in-backup-plan](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dynamodb-in-backup-plan.html)

### dynamodb-pitr-enabled

>ポイントインタイムリカバリ (PITR) が Amazon DynamoDB テーブルに対して有効になっていることを確認します。ポイントインタイムリカバリが Amazon DynamoDB テーブルに対して有効になっていない場合、ルールは NON_COMPLIANT です。
>[dynamodb-pitr-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dynamodb-pitr-enabled.html)

### DynamoDB-バックアップ計画によって保護されるリソース

>Amazon DynamoDB テーブルがバックアップ計画で保護されているかどうかを確認します。DynamoDB テーブルがバックアップ計画の対象でない場合、ルールは NON_COMPLIANT です。
>[DynamoDB-バックアップ計画によって保護されるリソース](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dynamodb-resources-protected-by-backup-plan.html)

### dynamodb-table-encrypted-kms

>Amazon DynamoDB テーブルが AWS Key Management Service (KMS) で暗号化されているかどうかを確認します。Amazon DynamoDB テーブルが AWS KMS で暗号化されていない場合、ルールは NON_COMPLIANT です。暗号化された AWS KMS キーが kmsKeyArns 入力パラメータに存在しない場合も、ルールは NON_COMPLIANT です。
>[dynamodb-table-encrypted-kms](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dynamodb-table-encrypted-kms.html)

### dynamodb-table-encryption-enabled

>Amazon DynamoDB テーブルが暗号化されているかどうか、およびそのステータスを確認します。ステータスが有効または有効化中の場合、ルールは COMPLIANT です。
>[dynamodb-table-encryption-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dynamodb-table-encryption-enabled.html)

### dynamodb-throughput-limit-check

>DynamoDB のプロビジョンドスループットがアカウントの上限に近づいているかどうかを確認します。デフォルトでは、このルールはプロビジョンドスループットがアカウント上限の 80% のしきい値を超えているかどうかを確認します。
>[dynamodb-throughput-limit-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/dynamodb-throughput-limit-check.html)

### ebs-in-backup-plan

>Amazon Elastic Block Store (Amazon EBS) ボリュームが AWS Backup のバックアッププランに追加されているかどうかを確認します。Amazon EBS ボリュームが Backup プランに含まれていない場合、ルールは NON_COMPLIANT です。
>[ebs-in-backup-plan](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ebs-in-backup-plan.html)

### ebs-optimized-instance

>EBS 最適化できる EC2 インスタンスに対して EBS 最適化が有効になっているかどうかを確認します。EBS 最適化できる EC2 インスタンスに対して EBS 最適化が有効化されていない場合、ルールは NON_COMPLIANT です。
>[ebs-optimized-instance](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ebs-optimized-instance.html)

### バックアップ計画によって保護された EBS リソース

>Amazon Elastic Block Store (Amazon EBS) ボリュームが、バックアップ計画に追加されているかどうかを確認します。Amazon EBSボリュームがバックアップ計画の対象でない場合、ルールは NON_COMPLIANT です。
>[バックアップ計画によって保護された EBS リソース](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ebs-resources-protected-by-backup-plan.html)

### ebs-snapshot-public-restorable-check

>Amazon Elastic Block Store (Amazon EBS) スナップショットがパブリックに復元不可能になっているかどうかを確認します。RestorableByUserIds フィールドを持つ 1 つ以上のスナップショットが「all」に設定されている場合、つまり Amazon EBS スナップショットがパブリックである場合、ルールは NON_COMPLIANT です。
>[ebs-snapshot-public-restorable-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ebs-snapshot-public-restorable-check.html)

### ec2-ebs-encryption-by-default

>Amazon Elastic Block Store (EBS) 暗号化がデフォルトで有効になっていることを確認します。暗号化が有効でない場合、ルールは NON_COMPLIANT です。
>[ec2-ebs-encryption-by-default](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-ebs-encryption-by-default.html)

### ec2-imdsv2-check

>Amazon Elastic Compute Cloud (Amazon EC2) インスタンスのメタデータのバージョンが、Instance Metadata Service Version 2 (IMDSv2) で設定されているかどうかを確認します。HttpTokens が「optional」に設定されている場合、ルールは NON_COMPLIANT です。
>[ec2-imdsv2-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-imdsv2-check.html)

### ec2-instance-detailed-monitoring-enabled

>詳細モニタリングが EC2 インスタンスに対して有効になっているかどうかを確認します。詳細モニタリングが有効になっていない場合、ルールは NON_COMPLIANT です。
>[ec2-instance-detailed-monitoring-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-instance-detailed-monitoring-enabled.html)

### ec2-instance-managed-by-systems-manager

>アカウント内の Amazon EC2 インスタンスが AWS Systems Manager によって管理されているかどうかを確認します。Amazon EC2 インスタンスが接続を失っている場合、ルールは NON_COMPLIANT になります。
>[ec2-instance-managed-by-systems-manager](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-instance-managed-by-systems-manager.html)

### ec2-instance-multiple-eni-check

>Amazon Elastic Compute Cloud (Amazon EC2) で複数の ENI (Elastic Network Interface) または Elastic Fabric Adapter (EFA) が使用されているかどうかを確認します。Amazon EC2 インスタンスで複数のネットワークインターフェイスが使用されている場合、このルールは NON_COMPLIANT です。
>[ec2-instance-multiple-eni-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-instance-multiple-eni-check.html)

### ec2-instance-no-public-ip

>Amazon Elastic Compute Cloud (Amazon EC2) インスタンスにパブリック IP の関連付けがあるかどうかを確認します。Amazon EC2 インスタンスの設定項目に publicIp フィールドが存在する場合、ルールは NON_COMPLIANT です。このルールは、IPv4 のみに適用されます。
>[ec2-instance-no-public-ip](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-instance-no-public-ip.html)

### ec2-instance-profile-attached

>Amazon Elastic Compute Cloud (Amazon EC2) インスタンスに Identity and Access Management (IAM) プロファイルがアタッチされているかどうかを確認します。IAM プロファイルが Amazon EC2 インスタンスにアタッチされていない場合、このルールは NON_COMPLIANT です。
>[ec2-instance-profile-attached](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-instance-profile-attached.html)

### ec2-managedinstance-applications-blacklisted

>指定したアプリケーションのいずれもインスタンスにインストールされていないことを確認します。必要に応じて、バージョンを指定します。新しいバージョンはブラックリストに記載されません。オプションで、プラットフォームを指定すると、このプラットフォームを実行しているインスタンスにのみルールが適用されます。
>[ec2-managedinstance-applications-blacklisted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-managedinstance-applications-blacklisted.html)

### ec2-managedinstance-applications-required

>すべての指定したアプリケーションが、インスタンスにインストールされているかどうかを確認します。オプションで、使用可能な最小バージョンを指定します。また、そのプラットフォームを実行中のインスタンスのみにルールを適用するプラットフォームを指定できます。
>[ec2-managedinstance-applications-required](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-managedinstance-applications-required.html)

### ec2-managedinstance-association-compliance-status-check

>インスタンスの関連付けが実行された後、AWS Systems Manager の関連付けのコンプライアンスステータスが COMPLIANT と NON_COMPLIANT のどちらであるかを確認します。フィールドステータスが COMPLIANT の場合は、ルールに準拠しています。関連付けの詳細については、「関連付けとは何ですか?」 を参照してください。
>[ec2-managedinstance-association-compliance-status-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-managedinstance-association-compliance-status-check.html)

### ec2-managedinstance-inventory-blacklisted

>Amazon EC2 Systems Manager が管理するインスタンスが、ブラックリストに記載されたインベントリタイプを収集するように設定されているかどうかを確認します。
>[ec2-managedinstance-inventory-blacklisted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-managedinstance-inventory-blacklisted.html)

### ec2-managedinstance-patch-compliance-status-check

>インスタンスでパッチのインストールが実行された後、AWS Systems Managers のパッチコンプライアンスのコンプライアンスステータスが COMPLIANT と NON_COMPLIANT のどちらであるかを確認します。フィールドステータスが COMPLIANT の場合は、ルールに準拠しています。
>[ec2-managedinstance-patch-compliance-status-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-managedinstance-patch-compliance-status-check.html)

### ec2-managedinstance-platform-check

>EC2 マネージドインスタンスの設定が希望どおりであるかどうかを確認します。
>[ec2-managedinstance-platform-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-managedinstance-platform-check.html)

### ec2-no-amazon-key-pair

>Amazon Elastic Compute Cloud (EC2) インスタンスがアマゾンキーペアを使用して起動されているかどうかを確認します。実行中の EC2 インスタンスが key pair で起動されている場合、ルールは NON_COMPLIANT です。
>[ec2-no-amazon-key-pair](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-no-amazon-key-pair.html)

### ec2-paravirtual-instance-check

>EC2 インスタンスの仮想化タイプが準仮想化かどうかをチェックします。「virtualizationType」が「paravirtual」に設定されている場合、EC2 インスタンスのこのルールは NON_COMPLIANT です。
>[ec2-paravirtual-instance-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-paravirtual-instance-check.html)

### ec2-resources-protected-by-backup-plan

>Amazon Elastic Compute Cloud (Amazon EC2) インスタンスがバックアップ計画で保護されているかどうかを確認します。Amazon EC2 インスタンスがバックアップ計画の対象でない場合、ルールは NON_COMPLIANT です。
>[ec2-resources-protected-by-backup-plan](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-resources-protected-by-backup-plan.html)

### ec2-security-group-attached-to-eni

>デフォルトではないセキュリティグループが Elastic Network Interface (ENI) にアタッチされているかどうかを確認します。そのセキュリティグループが Elastic Network Interface (ENI) に関連付けられていない場合、ルールは NON_COMPLIANT になります。
>[ec2-security-group-attached-to-eni](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-security-group-attached-to-eni.html)

### ec2-security-group-attached-to-eni-periodic

>デフォルトではないセキュリティグループが Elastic Network Interface (ENI) にアタッチされているかどうかを確認します。そのセキュリティグループが Elastic Network Interface (ENI) に関連付けられていない場合、ルールは NON_COMPLIANT になります。
>[ec2-security-group-attached-to-eni-periodic](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-security-group-attached-to-eni-periodic.html)

### ec2-stopped-instance

>許可されている日数よりも長く停止しているインスタンスがあるかどうかを確認します。ec2 インスタンスの状態が、許可されている日数より長く停止している場合、インスタンスは NON_COMPLIANT です。
>[ec2-stopped-instance](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-stopped-instance.html)

### ec2-token-hop-limit-check

>Amazon Elastic Compute Cloud (EC2) インスタンスメタデータに、希望する制限を下回る指定されたトークンホップ制限があるかどうかを確認します。ホップ制限値が意図した制限を超える場合、ルールはインスタンスに対して NON_COMPLIANT です。
>[ec2-token-hop-limit-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-token-hop-limit-check.html)

### ec2-transit-gateway-auto-vpc-attach-disabled

>Amazon Elastic Compute Cloud (Amazon EC2) トランジットゲートウェイで「AutoAcceptSharedAttachments」が有効になっているかどうかを確認します。「AutoAcceptSharedAttachments」が「有効」に設定されている場合、ルールは、トランジットゲートウェイに対して NON_COMPLIANT になります。
>[ec2-transit-gateway-auto-vpc-attach-disabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-transit-gateway-auto-vpc-attach-disabled.html)

### ec2-volume-inuse-check

>EBS ボリュームが EC2 インスタンスにアタッチされているかどうかを確認します。オプションで、インスタンスの削除時に EBS ボリュームが削除対象としてマークされるかどうかを確認します。
>[ec2-volume-inuse-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-volume-inuse-check.html)

### ecr-private-image-scanning-enabled

>プライベート Amazon Elastic Container Registry (ECR) リポジトリでイメージスキャンが有効化されているかどうかを確認します。プライベート ECR リポジトリに対してイメージスキャンが有効化されていない場合、ルールは NON_COMPLIANT になります。
>[ecr-private-image-scanning-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecr-private-image-scanning-enabled.html)

### ecr-private-lifecycle-policy-configured

>プライベート Amazon Elastic Container Registry (ECR) リポジトリに少なくとも 1 つのライフサイクルポリシーが設定されているかどうかを確認します。ECR プライベートリポジトリに対してライフサイクルポリシーが設定されていない場合、ルールは NON_COMPLIANT になります。
>[ecr-private-lifecycle-policy-configured](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecr-private-lifecycle-policy-configured.html)

### ecr-private-tag-immutability-enabled

>プライベート Amazon Elastic Container Registry (ECR) リポジトリでタグのイミュータビリティが有効化されているかどうかを確認します。プライベート ECR リポジトリに対してタグのイミュータビリティが有効化されていない場合、ルールは NON_COMPLIANT になります。
>[ecr-private-tag-immutability-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecr-private-tag-immutability-enabled.html)

### ecs-containers-nonprivileged

>ECSTaskDefinitions のコンテナの定義内にある特権パラメータが「true」に設定されているかどうかを確認します。特権パラメータが「true」の場合、ルールは NON_COMPLIANT になります。
>[ecs-containers-nonprivileged](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecs-containers-nonprivileged.html)

### ecs-containers-readonly-access

>Amazon Elastic Container Service (Amazon ECS) コンテナで、そのルートファイルシステムに対して読み取り専用アクセス権のみが設定されていることを確認します。ECSTaskDefinitions のコンテナの定義で readonlyRootFilesystem パラメータが「false」に設定されている場合、ルールは NON_COMPLIANT になります。
>[ecs-containers-readonly-access](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecs-containers-readonly-access.html)

### ecs-no-environment-secrets

>シークレットがコンテナ環境変数として渡されるかどうかを確認します。1 つ、または複数の環境変数キーが「secretKeys」パラメータにリストされているキーに一致する場合、ルールは NON_COMPLIANT になります (Amazon S3 などの他の場所からの環境変数を除く)。
>[ecs-no-environment-secrets](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecs-no-environment-secrets.html)

### ecs-task-definition-memory-hard-limit

>Amazon Elastic Container Service (ECS) のタスク定義に、そのコンテナの定義に対するメモリ制限が設定されているかどうかを確認します。1 つのコンテナの定義に「memory」パラメータが存在しない場合、タスク定義のルールは NON_COMPLIANT になります。
>[ecs-task-definition-memory-hard-limit](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecs-task-definition-memory-hard-limit.html)

### ecs-task-definition-nonroot-user

>ECSTaskDefinitions が、実行先の Amazon Elastic Container Service (Amazon ECS) の EC2 起動タイプコンテナにユーザーを指定するかどうかを確認します。「user」パラメータが存在しない、または「root」に設定されている場合、ルールは NON_COMPLIANT になります。
>[ecs-task-definition-nonroot-user](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecs-task-definition-nonroot-user.html)

### ecs-task-definition-pid-mode-check

>ECSTaskDefinitions が、ホストのプロセス名前空間をその Amazon Elastic Container Service (Amazon ECS) コンテナと共有するように設定されているかどうかを確認します。pidMode パラメータが「host」に設定されている場合、ルールは NON_COMPLIANT になります。
>[ecs-task-definition-pid-mode-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecs-task-definition-pid-mode-check.html)

### ecs-task-definition-user-for-host-mode-check

>ホストネットワークモードを使用する Amazon Elastic Container Service (Amazon ECS) のタスク定義に、「privileged」または「user」というコンテナ定義があるかどうかを確認します。ホストネットワークモードを使用するタスク定義と、privileged=false または空、user=root または空というコンテナ定義がある場合、ルールは NON_COMPLIANT です。
>[ecs-task-definition-user-for-host-mode-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ecs-task-definition-user-for-host-mode-check.html)

### efs-access-point-enforce-root-directory

>Amazon Elastic File System (Amazon EFS) アクセスポイントが、ルートディレクトリを適用するよう設定されているかどうかを確認します。「Path」の値が「'/'」(ファイルシステムのデフォルトのルートディレクトリ) に設定されている場合、ルールは NON_COMPLIANT です。
>[efs-access-point-enforce-root-directory](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/efs-access-point-enforce-root-directory.html)

### efs-access-point-enforce-user-identity

>Amazon Elastic File System (Amazon EFS) アクセスポイントが、ユーザー ID を適用するよう設定されているかどうかを確認します。「PosixUser」が定義されていない場合、またはパラメータが提供され、対応するパラメータに一致するものがない場合、ルールは NON_COMPLIANT です。
>[efs-access-point-enforce-user-identity](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/efs-access-point-enforce-user-identity.html)

### efs-encrypted-check

>Amazon Elastic File System (Amazon EFS) が、AWS Key Management Service (AWS KMS) を使用してファイルデータを暗号化するよう設定されているかどうかを確認します。暗号化されたキーが DescribeFileSystems で false に設定されている場合、または KmsKeyId の DescribeFileSystems キーが KmsKeyId パラメータと一致 しない場合、ルールは NON_COMPLIANT です。
>[efs-encrypted-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/efs-encrypted-check.html)

### efs-in-backup-plan

>Amazon Elastic File System (Amazon EFS) ファイルシステムが、AWS Backup のバックアッププランに追加されているかどうかを確認します。EFS ファイルシステムがバックアッププランに含まれていない場合、ルールは NON_COMPLIANT です。
>[efs-in-backup-plan](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/efs-in-backup-plan.html)

### バックアップ計画によって保護された efs リソース

>Amazon Elastic File System (Amazon EFS) ファイルシステムがバックアップ計画で保護されているかどうかを確認します。EFS ファイルがバックアップ計画の対象でない場合、ルールは NON_COMPLIANT です。
>[バックアップ計画によって保護された efs リソース](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/efs-resources-protected-by-backup-plan.html)

### eip-attached

>AWS アカウントに割り当てられたすべての Elastic IP アドレスが、EC2 インスタンスまたは使用中の Elastic Network Interface (ENI) にアタッチされているかどうかを確認します。
>[eip-attached](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/eip-attached.html)

### eks-cluster-oldest-supported-version

>Amazon Elastic Kubernetes Service (EKS) クラスターが、サポートされているバージョンで最も古いものを実行しているかどうかを確認します。EKS クラスターがサポートされている最も古いバージョンを実行している場合 (パラメータ 「oldestVersionSupported」に等しい)、ルールは NON_COMPLIANT になります。
>[eks-cluster-oldest-supported-version](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/eks-cluster-oldest-supported-version.html)

### eks-cluster-supported-version

>Amazon Elastic Kubernetes Service (EKS) クラスターが、サポートされている Kubernetes バージョンを実行しているかどうかを確認します。サポートされていないバージョン (パラメータ「oldestVersionSupported」未満) を EKS クラスターが使用している場合、このルールは NON_COMPLIANT になります。
>[eks-cluster-supported-version](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/eks-cluster-supported-version.html)

### eks-endpoint-no-public-access

>Amazon Elastic Kubernetes Service (Amazon EKS) エンドポイントがパブリックアクセス可能になっていないかどうかを確認します エンドポイントがパブリックである場合、ルールは NON_COMPLIANT です。
>[eks-endpoint-no-public-access](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/eks-endpoint-no-public-access.html)

### eks-secrets-encrypted

>Amazon Elastic Kubernetes Service クラスターが、AWS Key Management Service (KMS) キーを使用して Kubernetes シークレットを暗号化するように設定されているかどうかを確認します。
>[eks-secrets-encrypted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/eks-secrets-encrypted.html)

### elasticache-redis-cluster-automatic-backup-check

>Amazon ElastiCache Redis クラスターで自動バックアップが有効になっているかどうかを確認します。Redis クラスターの SnapshotRetentionLimit がSnapshotRetentionPeriod パラメータより小さい場合、ルールは NON_COMPLIANT です。例えば、パラメータが 15 の場合、snapshotRetentionPeriod が 0 ～ 15 であれば、ルールは準拠していません。
>[elasticache-redis-cluster-automatic-backup-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.html)

### elasticsearch-encrypted-at-rest

>Amazon OpenSearch Service (OpenSearch Service) ドメインで保管時の暗号化設定が有効になっているかどうかを確認します。EncryptionAtRestOptions フィールドが有効でない場合、ルールは NON_COMPLIANT です。
>[elasticsearch-encrypted-at-rest](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elasticsearch-encrypted-at-rest.html)

### elasticsearch-in-vpc-only

>Amazon OpenSearch Service (OpenSearch Service) ドメインが Amazon Virtual Private Cloud (VPC) 内にあるかどうかを確認します。OpenSearch Service ドメインのエンドポイントがパブリックである場合、ルールは NON_COMPLIANT になります。
>[elasticsearch-in-vpc-only](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elasticsearch-in-vpc-only.html)

### elasticsearch-logs-to-cloudwatch

>Amazon OpenSearch Service (OpenSearch Service) ドメインが、Amazon CloudWatch Logs にログを送信するように設定されているかどうかを確認します。OpenSearch Service ドメインに対してログが有効になっている場合、ルールは COMPLIANT です。ログ記録が設定されていない場合、このルールは NON_COMPLIANT です。
>[elasticsearch-logs-to-cloudwatch](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elasticsearch-logs-to-cloudwatch.html)

### elasticsearch-node-to-node-encryption-check

>Amazon OpenSearch Service ノードがエンドツーエンドで暗号化されていることを確認します。ノード間の暗号化がドメイン上で無効になっている場合、ルールは NON_COMPLIANT です。
>[elasticsearch-node-to-node-encryption-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elasticsearch-node-to-node-encryption-check.html)

### elastic-beanstalk-managed-updates-enabled

>AWS Elastic Beanstalk 環境の管理されたプラットフォームの更新が有効になっているかどうかを確認します。ManagedActionsEnabled の値が true に設定されている場合、ルールは COMPLIANT です。ManagedActionsEnabled の値が false に設定されている場合、またはパラメータが指定されているもののその値が既存の設定と一致しない場合、ルールは NON_COMPLIANT です。
>[elastic-beanstalk-managed-updates-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elastic-beanstalk-managed-updates-enabled.html)

### elbv2-acm-certificate-required

>Application Load Balancer と Network Load Balancer が、AWS Certificate Manager (ACM) の証明書を使用するように設定されているリスナーを持っているかどうかを確認します。少なくとも 1 つのロードバランサーに、ACM からの証明書を使用しないよう設定されている、または ACM 証明書とは異なる証明書を使用して設定されているリスナーが少なくとも 1 つある場合、このルールは NON_COMPLIANT です。
>[elbv2-acm-certificate-required](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elbv2-acm-certificate-required.html)

### elbv2-multiple-az

>Elastic Load Balancer V2 (アプリケーション、ネットワーク、または Gateway Load Balancer) に複数のアベイラビリティーゾーン (AZ) のインスタンスが登録されているかどうかを確認します。Elastic Load Balancer V2 のインスタンスが 2 AZ 未満に登録されている場合、ルールは NON_COMPLIANT です。
>[elbv2-multiple-az](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elbv2-multiple-az.html)

### elb-acm-certificate-required

>Classic Load Balancer が AWS Certificate Manager によって提供される SSL 証明書を使用しているかどうかを確認します。このルールを使用するには、Classic Load Balancer と共に SSL または HTTPS リスナーを使用する必要があります。このルールは、Classic Load Balancer にのみ適用されます。このルールは Application Load Balancer および Network Load Balancer を確認しません。
>[elb-acm-certificate-required](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elb-acm-certificate-required.html)

### elb-cross-zone-load-balancing-enabled

>クロスゾーンロードバランシングが Classic Load Balancer (CLB) に対して有効になっているかどうかを確認します。クロスゾーンロードバランシングが CLB に対して有効でない場合、このルールは NON_COMPLIANT です。
>[elb-cross-zone-load-balancing-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elb-cross-zone-load-balancing-enabled.html)

### elb-custom-security-policy-ssl-check

>Classic Load Balancer の SSL リスナーがカスタムポリシーを使用しているかどうか確認します。このルールは、Classic Load Balancer の SSL リスナーがある場合のみ適用されます。
>[elb-custom-security-policy-ssl-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elb-custom-security-policy-ssl-check.html)

### elb-deletion-protection-enabled

>Elastic Load Balancing で削除保護が有効になっているかどうかを確認します。deletion_protection.enabled が false の場合、ルールは NON_COMPLIANT です。
>[elb-deletion-protection-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elb-deletion-protection-enabled.html)

### elb-logging-enabled

>Application Load Balancer と Classic Load Balancer でログ記録が有効になっているかどうかを確認します。access_logs.s3.enabled が false で、access_logs.S3.bucket が入力した s3BucketName と同じでない場合、ルールは NON_COMPLIANT です。
>[elb-logging-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elb-logging-enabled.html)

### elb-predefined-security-policy-ssl-check

>Classic Load Balancer の SSL リスナーが事前定義済みポリシーを使用しているかどうか確認します。このルールは、Classic Load Balancer の SSL リスナーがある場合のみ適用されます。
>[elb-predefined-security-policy-ssl-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elb-predefined-security-policy-ssl-check.html)

### elb-tls-https-listeners-only

>Classic Load Balancer が SSL または HTTPS リスナーで設定されているかどうかを確認します。
>[elb-tls-https-listeners-only](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/elb-tls-https-listeners-only.html)

### emr-kerberos-enabled

>Amazon EMR クラスターで Kerberos が有効になっていることを確認します。セキュリティ構成がクラスターにアタッチされていない場合、またはセキュリティ構成が指定されたルールパラメータを満たしていない場合、ルールは NON_COMPLIANT です。
>[emr-kerberos-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/emr-kerberos-enabled.html)

### emr-master-no-public-ip

>Amazon Elastic MapReduce (EMR) クラスターのマスターノードにパブリック IP があるかどうかを確認します。マスターノードにパブリック IP がある場合、ルールは NON_COMPLIANT です。
>[emr-master-no-public-ip](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/emr-master-no-public-ip.html)

### encrypted-volumes

>アタッチ状態の EBS ボリュームが暗号化されているかどうかを確認します。kmsId パラメータを使用して暗号化に KMS キーの ID を指定した場合、ルールでは、アタッチ状態の EBS ボリュームが、その KMS キーで暗号化されているかどうか確認されます。
>[encrypted-volumes](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/encrypted-volumes.html)

### fms-shield-resource-policy-check

>Application Load Balancer、Amazon CloudFront ディストリビューション、Elastic Load Balancing、または Elastic IP が AWS Shield で保護されているかどうかを確認します。また、Application Load Balancer と Amazon CloudFront ディストリビューションにウェブ ACL が関連付けられているかどうかも確認します。
>[fms-shield-resource-policy-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/fms-shield-resource-policy-check.html)

### fms-webacl-resource-policy-check

>ウェブ ACL が、Application Load Balancer、API Gateway ステージ、または Amazon CloudFront ディストリビューションに関連付けられているかどうかを確認します。AWS Firewall Manager マネージャーがこのルールを作成すると、FMS ポリシー所有者は FMS ポリシーで WebACLId を指定し、オプションで修復を有効にできます。
>[fms-webacl-resource-policy-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/fms-webacl-resource-policy-check.html)

### fms-webacl-rulegroup-association-check

>ウェブ ACL に関連付けるルールグループに適切な優先順位が付けられていることを確認します。適切な優先度は、ruleGroups パラメータのルールグループのランクによって決定されます。AWS Firewall Manager ではこのルールを作成するときに、最も高い優先度 0 を割り当て、1、2 のように続けます。FMS ポリシー所有者は FMS ポリシーで ruleGroups ランクを指定し、必要に応じて修復を有効にできます。
>[fms-webacl-rulegroup-association-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/fms-webacl-rulegroup-association-check.html)

### fsx-resources-protected-by-backup-plan

>Amazon FSx ファイルシステムがバックアップ計画で保護されているかどうかを確認します。Amazon FSx ファイルがバックアップ計画の対象でない場合、ルールは NON_COMPLIANT です。
>[fsx-resources-protected-by-backup-plan](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/fsx-resources-protected-by-backup-plan.html)

### guardduty-enabled-centralized

>AWS アカウントとリージョンで Amazon GuardDuty が有効になっているかどうかを確認します。一元管理を目的として AWS アカウントを指定すると、ルールが一元管理されたアカウントの Amazon GuardDuty の結果を評価します。Amazon GuardDuty が有効になっている場合、ルールは COMPLIANT です。
>[guardduty-enabled-centralized](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/guardduty-enabled-centralized.html)

### guardduty-non-archived-findings

>Amazon GuardDuty にアーカイブされていない検出結果があるかどうかを確認します。Amazon GuardDuty に、daysLowSev/daysMediumSev/daysHighSev パラメータで指定されている値よりも古い、重要度が低/中/高のアーカイブされていない検出結果がある場合、ルールは NON_COMPLIANT です。
>[guardduty-non-archived-findings](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/guardduty-non-archived-findings.html)

### iam-customer-policy-blocked-kms-actions

>作成したマネージド AWS Identity and Access Management (IAM) ポリシーが、すべての AWS KMS キーでブロックされているアクションを許可していないことを確認します。AWS KMS キーでブロックされているアクションが、マネージド IAM ポリシーによって許可されている場合、ルールは NON_COMPLIANT です。
>[iam-customer-policy-blocked-kms-actions](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-customer-policy-blocked-kms-actions.html)

### iam-group-has-users-check

>IAM グループに少なくとも 1 人の IAM ユーザーが存在するかどうか確認します。
>[iam-group-has-users-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-group-has-users-check.html)

### iam-inline-policy-blocked-kms-actions

>IAM ユーザー、ロール、およびグループにアタッチされているインラインポリシーが、すべての AWS Key Management Service (KMS) キーでブロックされているアクションを許可していないことを確認します。インラインポリシーですべての KMS キーでブロックされているアクションが許可されている場合、ルールは NON_COMPLIANT です。
>[iam-inline-policy-blocked-kms-actions](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-inline-policy-blocked-kms-actions.html)

### iam-no-inline-policy-check

>インラインポリシー機能が使用されていないことを確認します。AWS Identity and Access Management (IAM) ユーザー、IAM ロール、または IAM グループにインラインポリシーがある場合、ルールは NON_COMPLIANT です
>[iam-no-inline-policy-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-no-inline-policy-check.html)

### iam-password-policy

>IAM ユーザーのアカウントパスワードポリシーが、パラメータで指定した要件を満たしているかどうかを確認します。アカウントのパスワードポリシーが指定の要件を満たしていない場合、このルールは NON_COMPLIANT です。
>[iam-password-policy](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-password-policy.html)

### iam-policy-blacklisted-check

>各 IAM リソースで、入力パラメータのポリシー ARN が IAM リソースにアタッチされているかどうかを確認します。ポリシー ARN が IAM リソースにアタッチされている場合、ルールは NON_COMPLIANT です。ポリシー ARN の有無にかかわらず、IAM リソースが exceptionList パラメータの一部である場合、AWS Config はリソースを COMPLIANT としてマークします。
>[iam-policy-blacklisted-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-policy-blacklisted-check.html)

### iam-policy-in-use

>IAM ポリシー ARN が、IAM ユーザー、1 人以上の IAM ユーザーを持つ IAM グループ、または 1 つ以上の信頼されたエンティティを持つ IAM ロールにアタッチされているかどうかを確認します。
>[iam-policy-in-use](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-policy-in-use.html)

### iam-policy-no-statements-with-admin-access

>作成したポリシーで、すべてのリソースのすべてのアクションにアクセス許可を付与する Allow ステートメントを確認します。いずれかのポリシーステートメントで、"Resource": "*" に対して "Action": "*" が "Effect": "Allow" になっている場合、ルールは NON_COMPLIANT です。
>[iam-policy-no-statements-with-admin-access](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-policy-no-statements-with-admin-access.html)

### iam-policy-no-statements-with-full-access

>AWS Identity and Access Management (IAM) ポリシーが個々の AWS リソースに対するすべてのアクションにアクセス許可を付与しているかどうかを確認します。マネージド IAM ポリシーが少なくとも 1 つの AWS のサービスへのフルアクセスを許可している場合、ルールは NON_COMPLIANT です。
>[iam-policy-no-statements-with-full-access](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-policy-no-statements-with-full-access.html)

### iam-role-managed-policy-check

>管理ポリシーのリストで指定されているすべての　AWS 管理ポリシーが、AWS　Identity and Access Management (IAM) ロールにアタッチされていることを確認します。IAM ロールに AWS 管理ポリシーがアタッチされていない場合、ルールは準拠していません。
>[iam-role-managed-policy-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-role-managed-policy-check.html)

### iam-root-access-key-check

>ルートユーザーアクセスキーがあるかどうかを確認します。ユーザーアクセスキーが存在しない場合、ルールは COMPLIANT です。それ以外の場合は、NON_COMPLIANTです。
>[iam-root-access-key-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-root-access-key-check.html)

### iam-user-group-membership-check

>IAM ユーザーが少なくとも 1 つの IAM グループのメンバーであるかどうかを確認します。
>[iam-user-group-membership-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-user-group-membership-check.html)

### iam-user-mfa-enabled

>AWS Identity and Access Management ユーザーの多要素認証 (MFA) が有効になっているかどうかを確認します。
>[iam-user-mfa-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-user-mfa-enabled.html)

### iam-user-no-policies-check

>いずれの IAM ユーザーにもポリシーがアタッチされていないことを確認します。IAM ユーザーは、IAM グループまたはロールからアクセス許可を継承する必要があります。ポリシーがアタッチされている IAM ユーザーが少なくとも 1 人いる場合、ルールは NONCOMPLIANT です。
>[iam-user-no-policies-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-user-no-policies-check.html)

### iam-user-unused-credentials-check

>AWS Identity and Access Management (IAM) ユーザーが、指定した日数以内に使用されていないパスワードまたはアクティブなアクセスキーを持っているかどうかを確認します。最近使用されていない非アクティブアカウントがある場合、ルールは NON_COMPLIANT です。
>[iam-user-unused-credentials-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/iam-user-unused-credentials-check.html)

### restricted-ssh

>セキュリティグループの受信 SSH トラフィックがアクセス可能かどうかを確認します。セキュリティグループの受信 SSH トラフィックの IP アドレスが制限されている場合 (0.0.0.0/0 以外の CIDR)、ルールは COMPLIANT です。このルールは、IPv4 のみに適用されます。
>[restricted-ssh](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/restricted-ssh.html)

### ec2-instances-in-vpc

>EC2 インスタンスが Virtual Private Cloud (VPC) に属しているかどうかを確認します。オプションで、インスタンスに関連付ける VPC ID を指定できます。
>[ec2-instances-in-vpc](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ec2-instances-in-vpc.html)

### internet-gateway-authorized-vpc-only

>インターネットゲートウェイ (IGW) が、承認された Amazon Virtual Private Cloud (VPC) にのみアタッチされていることを確認します。IGW が承認された VPC にアタッチされていない場合、ルールは NON_COMPLIANT です。
>[internet-gateway-authorized-vpc-only](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/internet-gateway-authorized-vpc-only.html)

### kinesis-stream-encrypted

>Amazon Kinesis Streams がサーバー側の暗号化を使用して保存時に暗号化されているかどうかを確認します。「StreamEncryption」が存在しない場合、ルールは Kinesis ストリームに対して NON_COMPLIANT になります。
>[kinesis-stream-encrypted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/kinesis-stream-encrypted.html)

### kms-cmk-not-scheduled-for-deletion

>AWS KMS keys(KMS キー) がAWS Key Management Service(AWS KMS)で削除するようにスケジュールされていないかを確認します。KMS の()で削除するようにスケジュールされている場合、ルールは NON_COMPLIANT です。
>[kms-cmk-not-scheduled-for-deletion](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/kms-cmk-not-scheduled-for-deletion.html)

### lambda-concurrency-check

>AWS Lambda 関数に関数レベルの同時実行数制限が設定されているかどうかを確認します。Lambda 関数に関数レベルの同時実行数制限が設定されていない場合、ルールは NON_COMPLIANT です。
>[lambda-concurrency-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/lambda-concurrency-check.html)

### lambda-dlq-check

>AWS Lambda 関数にデッドレターキューが設定されているかどうかを確認します。Lambda 関数にデッドレターキューが設定されていない場合、ルールは NON_COMPLIANT です。
>[lambda-dlq-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/lambda-dlq-check.html)

### lambda-function-public-access-prohibited

>Lambda リソースにアタッチされている AWS Lambda 関数ポリシーがパブリックアクセスを禁止しているかどうかを確認します。Lambda 関数ポリシーがパブリックアクセスを許可している場合、ルールは NON_COMPLIANT です。
>[lambda-function-public-access-prohibited](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/lambda-function-public-access-prohibited.html)

### lambda-function-settings-check

>ランタイム、ロール、タイムアウト、およびメモリサイズの AWS Lambda 関数設定が、予期されている値と一致するかどうか確認します。このルールは、「Image」パッケージタイプを含む関数を無視します。
>[lambda-function-settings-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/lambda-function-settings-check.html)

### lambda-inside-vpc

>AWS Lambda 関数による Amazon Virtual Private Cloud へのアクセスが許可されているかどうかを確認します。Lambda 関数で VPC が有効になっていない場合、ルールは NON_COMPLIANT です。
>[lambda-inside-vpc](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/lambda-inside-vpc.html)

### lambda-vpc-multi-az-check

>Lambda に複数のアベイラビリティーゾーンが関連付けられているかどうかを確認します。Lambda に 1 つのアベイラビリティーゾーンしか関連付けられていない場合、または関連付けられているアベイラビリティーゾーンの数がオプションのパラメータで指定されている数より少ない場合、ルールは NON_COMPLIANT になります。
>[lambda-vpc-multi-az-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/lambda-vpc-multi-az-check.html)

### mfa-enabled-for-iam-console-access

>コンソールパスワードを使用するすべての AWS Identity and Access Management (IAM) ユーザーに対して、AWS多要素認証 (MFA) が有効になっているかどうかを確認します。MFA が有効の場合、このルールは COMPLIANT です。
>[mfa-enabled-for-iam-console-access](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/mfa-enabled-for-iam-console-access.html)

### multi-region-cloudtrail-enabled

>マルチリージョン AWS CloudTrail が少なくとも 1 つあることを確認します。追跡が入力パラメータと一致しない場合、ルールは NON_COMPLIANT です。ExcludeManagementEventSourcesフィールドが空でない場合、またはAWSCloudTrail は、AWS KMSイベントまたは Amazon RDS データ API イベントのような管理イベントを除外するように構成される場合、ルールは NON_COMPLIANT です。
>[multi-region-cloudtrail-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/multi-region-cloudtrail-enabled.html)

### nacl-no-unrestricted-ssh-rdp

>ネットワークアクセスコントロールリスト (NACL) の SSH/RDP 受信トラフィックに対するデフォルトポートが制限なしかどうかを確認します。NACL インバウンドエントリがポート 22 または 3389 についてソース TCP または UDP CIDR ブロックを許可する場合、ルールは NON_COMPLIANT になります。
>[nacl-no-unrestricted-ssh-rdp](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/nacl-no-unrestricted-ssh-rdp.html)

### netfw-stateless-rule-group-not-empty

>ステートレスネットワークファイアウォールのルールグループにルールが含まれているかどうかを確認します。ステートレスネットワークファイアウォールのルールグループにルールがない場合、ルールは NON_COMPLIANT になります。
>[netfw-stateless-rule-group-not-empty](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/netfw-stateless-rule-group-not-empty.html)

### no-unrestricted-route-to-igw

>ルートテーブルにインターネットゲートウェイ (IGW) へのパブリックルートがあるかどうかを確認します。IGW へのルートに「0.0.0.0/0」または「። /0」などの送信先 CIDR ブロックがある場合、または送信先 CIDR ブロックがルールパラメータと一致しない場合、ルールは NON_COMPLIANT です。
>[no-unrestricted-route-to-igw](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/no-unrestricted-route-to-igw.html)

### opensearch-access-control-enabled

>きめ細かなアクセスコントロールが Amazon OpenSearch Service ドメインに設定されているかどうかをチェックします。AdvancedSecurityOptions が OpenSearch Service ドメインに対して有効になっていない場合、ルールは NON_COMPLIANT です。
>[opensearch-access-control-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/opensearch-access-control-enabled.html)

### opensearch-audit-logging-enabled

>Amazon OpenSearch Service ドメインで監査ログが有効になっているかどうかを確認します。OpenSearch Service ドメインで監査ログが有効になっていない場合、ルールは NON_COMPLIANT です。
>[opensearch-audit-logging-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/opensearch-audit-logging-enabled.html)

### opensearch-data-node-fault-tolerance

>Amazon OpenSearch Serviceのドメインが少なくとも 3 つのデータノードで構成され、zoneAwarenessEnabled が true であるかどうかをチェックします。'instanceCount' が 3 より小さい場合、または 'zoneAwarenessEnabled' が 'false' に設定されている場合、OpenSearch ドメインのルールは NON_COMPLIANT です。
>[opensearch-data-node-fault-tolerance](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/opensearch-data-node-fault-tolerance.html)

### opensearch-encrypted-at-rest

>Amazon OpenSearch Service ドメインで保管時の暗号化設定が有効になっているかどうかを確認します。EncryptionAtRestOptions フィールドが有効でない場合、ルールは NON_COMPLIANT です。
>[opensearch-encrypted-at-rest](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/opensearch-encrypted-at-rest.html)

### opensearch-https-required

>OpenSearch ドメインへの接続が HTTPS を使用しているかどうかをチェックします。Amazon OpenSearch ドメイン 'EnforceHTTPS' が 'true' でない場合、または 'true' であって 'TLSSecurityPolicy' が 'tlsPolicies' でない場合、ルールは NON_COMPLIANT です。
>[opensearch-https-required](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/opensearch-https-required.html)

### opensearch-in-vpc-only

>Amazon OpenSearch Service ドメインが Amazon Virtual Private Cloud (VPC) 内にあるかどうかを確認します。OpenSearch Service ドメインのエンドポイントがパブリックである場合、ルールは NON_COMPLIANT になります。
>[opensearch-in-vpc-only](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/opensearch-in-vpc-only.html)

### opensearch-logs-to-cloudwatch

>Amazon OpenSearch Service ドメインが、Amazon CloudWatch Logs にログを送信するように設定されているかどうかを確認します。ログ記録が設定されていない場合、ルールは NON_COMPLIANT です。
>[opensearch-logs-to-cloudwatch](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/opensearch-logs-to-cloudwatch.html)

### opensearch-node-to-node-encryption-check

>Amazon OpenSearch Service ノードがエンドツーエンドで暗号化されていることを確認します。ノード間の暗号化がドメイン上で有効になっていない場合、ルールは NON_COMPLIANT です。
>[opensearch-node-to-node-encryption-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/opensearch-node-to-node-encryption-check.html)

### rds-automatic-minor-version-upgrade-enabled

>Amazon Relational Database Service (RDS) データベースインスタンスが、自動マイナーバージョンアップグレードに設定されているかどうかを確認します。「autoMinorVersionUpgrade」の値が false の場合、ルールは NON_COMPLIANT です。
>[rds-automatic-minor-version-upgrade-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-automatic-minor-version-upgrade-enabled.html)

### rds-cluster-default-admin-check

>Amazon Relational Database Service (Amazon RDS) データベースクラスターが管理者ユーザーネームをそのデフォルト値から変更したかどうかを確認します。管理者ユーザーネームがデフォルト値に設定されている場合、ルールは NON_COMPLIANT になります。
>[rds-cluster-default-admin-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-cluster-default-admin-check.html)

### rds-cluster-deletion-protection-enabled

>Amazon Relational Database Service (Amazon RDS) クラスターで削除保護が有効になっているかどうかを確認します。RDS クラスターで削除保護が有効になっていない場合、ルールは NON_COMPLIANT です。
>[rds-cluster-deletion-protection-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-cluster-deletion-protection-enabled.html)

### rds-cluster-iam-authentication-enabled

>Amazon RDS クラスターで AWS Identity and Access Management (IAM) 認証が有効になっているかどうかを確認します。RDS クラスターで IAM 認証が有効になっていない場合、ルールは NON_COMPLIANT です。
>[rds-cluster-iam-authentication-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-cluster-iam-authentication-enabled.html)

### rds-cluster-multi-az-enabled

>Amazon Relational Database Service (Amazon RDS) によって管理される Amazon Aurora および Hermes クラスターで、マルチ AZ レプリケーションが有効になっているかどうかを確認します。Amazon RDS インスタンスがマルチ AZ を使用して設定されていない場合、ルールは NON_COMPLIANT です。
>[rds-cluster-multi-az-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-cluster-multi-az-enabled.html)

### rds-db-security-group-not-allowed

>デフォルトの DB セキュリティグループではない Amazon Relational Database Service (RDS) DB セキュリティグループが存在するかどうかを確認します。デフォルトの DB セキュリティグループではない DB セキュリティグループが存在する場合、ルールは NON_COMPLIANT になります。
>[rds-db-security-group-not-allowed](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-db-security-group-not-allowed.html)

### rds-enhanced-monitoring-enabled

>Amazon Relational Database Service (Amazon RDS) インスタンスに対して拡張モニタリングが有効になっているかどうかを確認します。
>[rds-enhanced-monitoring-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-enhanced-monitoring-enabled.html)

### rds-instance-default-admin-check

>Amazon Relational Database Service (Amazon RDS) データベースが管理者ユーザーネームをそのデフォルト値から変更したかどうかを確認します。このルールが実行されるのは RDS データベースインスタンスのみです。管理者ユーザーネームがデフォルト値に設定されている場合、ルールは NON_COMPLIANT になります。
>[rds-instance-default-admin-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-instance-default-admin-check.html)

### rds-instance-deletion-protection-enabled

>Amazon Relational Database Service (Amazon RDS) インスタンスで削除保護が有効になっているかどうかを確認します。Amazon RDS インスタンスで削除保護が有効になっていない場合、つまり deletionProtection が false に設定されている場合、このルールは NON_COMPLIANT です。
>[rds-instance-deletion-protection-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-instance-deletion-protection-enabled.html)

### rds-instance-iam-authentication-enabled

>Amazon Relational Database Service (Amazon RDS) インスタンスで AWS Identity and Access Management (IAM) 認証が有効になっているかどうかを確認します。Amazon RDS インスタンスで AWS IAM 認証が有効になっていない場合、つまり、configuration.iAMDatabaseAuthenticationEnabled が false に設定されている場合、このルールは NON_COMPLIANT です。
>[rds-instance-iam-authentication-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-instance-iam-authentication-enabled.html)

### rds-instance-public-access-check

>Amazon Relational Database Service インスタンスがパブリックアクセス可能になっていないかどうかを確認します インスタンスの設定項目で publiclyAccessible フィールドが true の場合、ルールは NON_COMPLIANT です。
>[rds-instance-public-access-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-instance-public-access-check.html)

### rds-in-backup-plan

>Amazon RDS データベースが AWS Backup のバックアッププランに存在しているかどうかを確認します。Amazon RDS データベースがどの AWS Backup のバックアッププランにも存在していない場合、ルールは NON_COMPLIANT です。
>[rds-in-backup-plan](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-in-backup-plan.html)

### rds-logging-enabled

>Amazon Relational Database Service (Amazon RDS) インスタンスの Amazon CloudWatch にエクスポートされたログタイプが有効になっているかどうかを確認します。このログタイプが有効でない場合、ルールは NON_COMPLIANT です。
>[rds-logging-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-logging-enabled.html)

### rds-multi-az-support

>RDS DB インスタンスの高可用性が有効になっているかどうかを確認します。
>[rds-multi-az-support](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-multi-az-support.html)

### rds-resources-protected-by-backup-plan

>Amazon Relational Database Service (Amazon RDS) インスタンスがバックアップ計画で保護されているかどうかを確認します。Amazon RDS データベースインスタンスがバックアップ計画の対象でない場合、ルールは NON_COMPLIANT です。
>[rds-resources-protected-by-backup-plan](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-resources-protected-by-backup-plan.html)

### rds-snapshots-public-prohibited

>Amazon Relational Database Service (Amazon RDS) スナップショットがパブリックかどうかを確認します。既存および新規の Amazon RDS スナップショットがパブリックである場合、ルールは NON_COMPLIANT です。
>[rds-snapshots-public-prohibited](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-snapshots-public-prohibited.html)

### rds-snapshot-encrypted

>Amazon Relational Database Service (Amazon RDS) DB スナップショットが暗号化されているかどうかを確認します。Amazon RDS DB スナップショットが暗号化されていない場合、ルールは NON_COMPLIANT です。
>[rds-snapshot-encrypted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-snapshot-encrypted.html)

### rds-storage-encrypted

>RDS DB インスタンスに対してストレージの暗号化が有効になっているかどうかを確認します。
>[rds-storage-encrypted](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/rds-storage-encrypted.html)

### redshift-backup-enabled

>Amazon Redshift 自動スナップショットがクラスターに対して有効になっていることを確認します。automatedSnapshotRetentionPeriod の値が MaxRetentionPeriod より大きいか MinRetentionPeriod より小さい場合、または値が 0 の場合、ルールは NON_COMPLIANT です。
>[redshift-backup-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-backup-enabled.html)

### redshift-cluster-configuration-check

>Amazon Redshift クラスターに指定された設定があるかどうか確認します。
>[redshift-cluster-configuration-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-cluster-configuration-check.html)

### redshift-cluster-kms-enabled

>Amazon Redshift クラスターが指定された AWS Key Management Service (AWS KMS) キーを使用して暗号化されているかどうかを確認します。暗号化が有効になっていて、クラスターが kmsKeyArn パラメータで指定されたキーで暗号化されている場合、ルールは COMPLIANT です。クラスターが暗号化されていない場合、または別のキーで暗号化されている場合、ルールは NON_COMPLIANT です。
>[redshift-cluster-kms-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-cluster-kms-enabled.html)

### redshift-cluster-maintenancesettings-check

>Amazon Redshift クラスターに、指定されたメンテナンス設定があるかどうか確認します。
>[redshift-cluster-maintenancesettings-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-cluster-maintenancesettings-check.html)

### redshift-cluster-public-access-check

>Amazon Redshift クラスターがパブリックアクセス可能になっていないかどうかを確認します。クラスターの設定項目で publiclyAccessible フィールドが true の場合、ルールは NON_COMPLIANT です。
>[redshift-cluster-public-access-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-cluster-public-access-check.html)

### redshift-default-admin-check

>Amazon Redshift クラスターが管理者ユーザーネームをそのデフォルト値から変更したかどうかを確認します。Redshift クラスターの管理ユーザーネームが「awsuser」に設定されている、またはユーザーネームがパラメータにリストされているものと一致しない場合、ルールは NON_COMPLIANT になります。
>[redshift-default-admin-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-default-admin-check.html)

### redshift-default-db-name-check

>Redshift クラスターがデータベース名をそのデフォルト値から変更したかどうかを確認します。Redshift クラスターのデータベース名が「dev」に設定されている場合、またはオプションのパラメータが指定されているのにデータベース名が一致しない場合、ルールは NON_COMPLIANT です。
>[redshift-default-db-name-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-default-db-name-check.html)

### redshift-enhanced-vpc-routing-enabled

>Amazon Redshift クラスターで「enhancedVpcRouting」が有効になっているかどうかを確認します。「enhancedVpcRouting」が有効でない場合、または configuration.enhancedVpcRouting フィールドが「false」の場合、ルールは NON_COMPLIANT です。
>[redshift-enhanced-vpc-routing-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-enhanced-vpc-routing-enabled.html)

### redshift-require-tls-ssl

>Amazon Redshift クラスターで SQL クライアントに接続するための TLS/SSL 暗号化が必要であるかどうかを確認します。Amazon Redshift クラスターでパラメータの require_SSL が true に設定されていない場合、ルールは NON_COMPLIANT です。
>[redshift-require-tls-ssl](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/redshift-require-tls-ssl.html)

### required-tags

>指定したタグがリソースにあるかどうかを確認します。例えば、Amazon EC2 インスタンスに CostCenter タグがあるかどうかを確認できます。複数の値はカンマで区切ります。一度に確認できるタグは 6 つまでです。
>[required-tags](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/required-tags.html)

### restricted-common-ports

>使用中のセキュリティグループが、指定されたポートへの制限されていない受信 TCP トラフィックを不許可にしているかどうかを確認します。受信 TCP 接続の IP アドレスが指定されたポートに制限されている場合、このルールは COMPLIANT です。このルールは、IPv4 のみに適用されます。
>[restricted-common-ports](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/restricted-common-ports.html)

### root-account-hardware-mfa-enabled

>AWS アカウントが、多要素認証 (MFA) ハードウェアデバイスを使用して、ルート認証情報でサインインできるようになっているかどうかを確認します。このルールは、ルート認証情報でサインインすることが許可されている仮想 MFA デバイスがあれば NON_COMPLIANT です。
>[root-account-hardware-mfa-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/root-account-hardware-mfa-enabled.html)

### root-account-mfa-enabled

>AWS アカウントのルートユーザーが多要素認証を使用してコンソールにサインインする必要があるかどうかを確認します。
>[root-account-mfa-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/root-account-mfa-enabled.html)

### s3-account-level-public-access-blocks

>必要なパブリックアクセスブロック設定がアカウントレベルから設定されているかどうかを確認します。以下に設定されているフィールドが、設定項目の対応するフィールドと一致しない場合、ルールは NON_COMPLIANT のみです。
>[s3-account-level-public-access-blocks](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-account-level-public-access-blocks.html)

### s3-account-level-public-access-blocks-periodic

>必要なパブリックアクセスのブロック設定がアカウントレベルから設定されているかどうかを確認します。
>[s3-account-level-public-access-blocks-periodic](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-account-level-public-access-blocks-periodic.html)

### s3-bucket-acl-prohibited

>Amazon Simple Storage Service (Amazon S3) バケットが、アクセスコントロールリスト (ACL) 経由でのユーザー許可を許容するかどうかを確認します。Amazon S3 バケットでのユーザーアクセスに ACL が設定されている場合、ルールは NON_COMPLIANT になります。
>[s3-bucket-acl-prohibited](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-acl-prohibited.html)

### s3-bucket-blacklisted-actions-prohibited

>Amazon Simple Storage Service バケットポリシーが、ブラックリストに登録されたバケットレベルおよびオブジェクトレベルのアクションを、バケット内のリソースで他の AWS アカウントのプリンシパルに対して実行することを許可していないことを確認します。例えば、このルールでは、Amazon S3 バケットポリシーが、別の AWS アカウントのバケット内のオブジェクトで s3:GetBucket* アクションと s3:DeleteObject のいずれの実行も許可していないことを確認します。ブラックリストに登録されているアクションが Amazon S3 バケットポリシーによって許可されている場合、ルールは NON_COMPLIANT です。
>[s3-bucket-blacklisted-actions-prohibited](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-blacklisted-actions-prohibited.html)

### s3-bucket-default-lock-enabled

>Amazon S3 バケットのロックが デフォルトで有効になっているかどうかを確認します。ロックが有効でない場合、ルールは NON_COMPLIANT です。
>[s3-bucket-default-lock-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-default-lock-enabled.html)

### s3-bucket-level-public-access-prohibited

>Amazon Simple Storage Service (Amazon S3) バケットがパブリックアクセス可能かどうかを確認します。Amazon S3 バケットが excludedPublicBuckets パラメータとバケットレベルの設定にリストされていない場合、このルールは NON_COMPLIANT です。
>[s3-bucket-level-public-access-prohibited](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-level-public-access-prohibited.html)

### s3-bucket-logging-enabled

>S3 バケットに対してログ記録が有効になっているかどうか確認します。
>[s3-bucket-logging-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-logging-enabled.html)

### s3-bucket-policy-grantee-check

>Amazon S3 バケットによって許可されたアクセスが、指定した任意の AWS プリンシパル、フェデレーティッドユーザー、サービスプリンシパル、IP アドレス、または VPC によって制限されていることを確認します。バケットポリシーが存在しない場合、ルールは COMPLIANT です。
>[s3-bucket-policy-grantee-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-policy-grantee-check.html)

### s3-bucket-policy-not-more-permissive

>Amazon Simple Storage Service バケットポリシーが、指定するコントロール Amazon S3 バケットポリシー以外でアカウント間の他のアクセスを許可していないことを確認します。
>[s3-bucket-policy-not-more-permissive](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-policy-not-more-permissive.html)

### s3-bucket-public-read-prohibited

>Amazon S3 バケットでパブリック読み取りアクセスが許可されていないかどうかを確認します。このルールは、パブリックアクセスのブロック設定、バケットポリシー、およびバケットアクセスコントロールリスト (ACL) を確認します。
>[s3-bucket-public-read-prohibited](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-public-read-prohibited.html)

### s3-bucket-public-write-prohibited

>Amazon S3 バケットでパブリック書き込みアクセスが許可されていないかどうかを確認します。このルールは、パブリックアクセスのブロック設定、バケットポリシー、およびバケットアクセスコントロールリスト (ACL) を確認します。
>[s3-bucket-public-write-prohibited](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-public-write-prohibited.html)

### s3-bucket-replication-enabled

>Amazon S3 バケットでクロスリージョンレプリケーションが有効になっているかどうかを確認します。
>[s3-bucket-replication-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-replication-enabled.html)

### s3-bucket-server-side-encryption-enabled

>Amazon S3 バケットで S3 のデフォルトの暗号化が有効になっていること、または S3 バケットポリシーが AES-256 または put-object を使用するサーバー側の暗号化を使用していない AWS Key Management Service リクエストを明示的に拒否することを確認します。Amazon S3 バケットが、デフォルトで暗号化されていない場合、ルールは NON_COMPLIANT です。
>[s3-bucket-server-side-encryption-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html)

### s3-bucket-ssl-requests-only

>Amazon S3 バケットに、Secure Socket Layer (SSL) を使用するリクエストを要求するポリシーがあるかどうか確認します。HTTP リクエストへのアクセスを明示的に拒否する場合、ルールは COMPLIANT です。バケットポリシーが HTTP リクエストを許可している場合、ルールは NON_COMPLIANT です。
>[s3-bucket-ssl-requests-only](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-ssl-requests-only.html)

### s3-bucket-versioning-enabled

>S3 バケットに対してバージョニングが有効になっているかどうかを確認します。オプションで、S3 バケットに対して MFA 削除が有効になっているかどうかを確認します。
>[s3-bucket-versioning-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-bucket-versioning-enabled.html)

### s3-default-encryption-kms

>Amazon S3 バケットが AWS Key Management Service (AWS KMS) で暗号化されているかどうかを確認します。Amazon S3 バケットが AWS KMS キーで暗号化されていない場合、ルールは NON_COMPLIANT です。
>[s3-default-encryption-kms](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-default-encryption-kms.html)

### s3-event-notifications-enabled

>S3 バケットで Amazon S3 イベント通知が有効になっているかどうかを確認します。S3 イベント通知がバケットに設定されていない場合、またはイベントタイプまたは宛先が eventTypes および destinationArn パラメータと一致しない場合、ルールは NON_COMPLIANT になります。
>[s3-event-notifications-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-event-notifications-enabled.html)

### s3-version-lifecycle-policy-check

>Amazon Simple Storage Service (Amazon S3) のバージョニングが有効化されたバケットにライフサイクルポリシーが設定されているかどうかを確認します。Amazon S3 ライフサイクルポリシーが有効化されていない場合、ルールは NON_COMPLIANT になります。
>[s3-version-lifecycle-policy-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/s3-version-lifecycle-policy-check.html)

### sagemaker-endpoint-configuration-kms-key-configured

>Amazon SageMaker エンドポイント設定に対して AWS Key Management Service (KMS) キーが設定されているかどうかを確認します。Amazon SageMaker エンドポイントの設定に対して 'KmsKeyId' が指定されていない場合、ルールは NON_COMPLIANT です。
>[sagemaker-endpoint-configuration-kms-key-configured](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/sagemaker-endpoint-configuration-kms-key-configured.html)

### sagemaker-notebook-instance-kms-key-configured

>Amazon SageMaker ノートブックインスタンスに対して AWS Key Management Service (KMS) キーが設定されているかどうかを確認します。Amazon SageMaker ノートブックインスタンスに対して 'KmsKeyId' が指定されていない場合、ルールは NON_COMPLIANT です。
>[sagemaker-notebook-instance-kms-key-configured](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/sagemaker-notebook-instance-kms-key-configured.html)

### sagemaker-notebook-no-direct-internet-access

>Amazon SageMaker ノートブックインスタンスで直接インターネットアクセスが無効になっているかどうかを確認します。Amazon SageMaker ノートブックインスタンスがインターネット対応の場合、ルールは NON_COMPLIANT です。
>[sagemaker-notebook-no-direct-internet-access](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/sagemaker-notebook-no-direct-internet-access.html)

### secretsmanager-rotation-enabled-check

>AWS Secrets Manager のシークレットでローテーションが有効になっているかどうかを確認します。このルールでは、オプションの maximumAllowedRotationFrequency パラメータも確認されます。パラメータが指定されている場合、シークレットのローテーション頻度が最大許容頻度と比較されます。シークレットのローテーションがスケジュールされていない場合、ルールは NON_COMPLIANT です。ローテーション頻度が maximumAllowedRotationFrequency パラメータで指定された数よりも高い場合も、ルールは NON_COMPLIANT になります。
>[secretsmanager-rotation-enabled-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/secretsmanager-rotation-enabled-check.html)

### secretsmanager-scheduled-rotation-success-check

>AWS Secrets Manager のシークレットのローテーションが、ローテーションスケジュールに従って正常にトリガー/開始されたかどうかを確認します。RotationOccurringAsScheduled が false の場合、ルールは NON_COMPLIANT です。
>[secretsmanager-scheduled-rotation-success-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.html)

### secretsmanager-secret-periodic-rotation

>AWS Secrets Manager のシークレットが過去に指定された日数でローテーションされているかどうかを確認します。シークレットが 「maxDaysSinceRotation」の日数を超えてもローテーションされていない場合、ルールは NON_COMPLIANT です。デフォルト値は 90 日です。
>[secretsmanager-secret-periodic-rotation](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/secretsmanager-secret-periodic-rotation.html)

### secretsmanager-secret-unused

>AWS Secrets Manager のシークレットが、指定された日数以内にアクセスされているかどうかを確認します。シークレットが 'unusedForDays' の日数以内にアクセスされていない場合、ルールは NON_COMPLIANT です。デフォルト値は 90 日です。
>[secretsmanager-secret-unused](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/secretsmanager-secret-unused.html)

### secretsmanager-using-cmk

>AWS Secrets Managerの すべてのシークレットを — AWS マネージドキー (aws/secretsmanager)、または AWS Key Management Service(AWS KMS)で作成したカスタマーマネージド型キーを使用して、暗号化しているかどうかを確認します。シークレットが、カスタマーマネージド型キーを使用して暗号化されている場合、このルールは COMPLIANT です。シークレットが aws/secretsmanager を使用して暗号化されている場合、このルールは COMPLIANT です。
>[secretsmanager-using-cmk](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/secretsmanager-using-cmk.html)

### securityhub-enabled

>AWS アカウントに対して AWS Security Hub が有効になっていることを確認します。AWS Security Hub が有効でない場合、ルールは NON_COMPLIANT です。
>[securityhub-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/securityhub-enabled.html)

### service-vpc-endpoint-enabled

>ルールパラメータで指定されたサービスのサービスエンドポイントが Amazon VPC ごとに作成されるかどうかを確認します。サービス用に作成された VPC エンドポイントが Amazon VPC にない場合、ルールは NON_COMPLIANT を返します。
>[service-vpc-endpoint-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/service-vpc-endpoint-enabled.html)

### shield-advanced-enabled-autorenew

>AWS アカウントで AWS Shield Advanced が有効になっていて、サブスクリプションが自動的に更新されるように設定されているかどうかを確認します。
>[shield-advanced-enabled-autorenew](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/shield-advanced-enabled-autorenew.html)

### shield-drt-access

>Shield レスポンスチーム (SRT) がお使いの AWS アカウントにアクセスできるかどうかを確認します。AWS Shield Advanced が有効になっていても SRT アクセスのロールが設定されていない場合、ルールは NON_COMPLIANT です。
>[shield-drt-access](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/shield-drt-access.html)

### sns-encrypted-kms

>Amazon SNS トピックが AWS Key Management Service (AWS KMS) で暗号化されているかどうかを確認します。Amazon SNS トピックが AWS KMS で暗号化されていない場合、ルールは NON_COMPLIANT です。暗号化された KMS キーが kmsKeyIds 入力パラメータに存在しない場合も、ルールは NON_COMPLIANT です。
>[sns-encrypted-kms](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/sns-encrypted-kms.html)

### sns-topic-message-delivery-notification-enabled

>エンドポイントのトピックに送信される通知メッセージの配信ステータスについて、Amazon Simple Notification Service (SNS) ログが有効になっているかどうかを確認します。メッセージの配信ステータス通知が有効でない場合、ルールは NON_COMPLIANT です。
>[sns-topic-message-delivery-notification-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/sns-topic-message-delivery-notification-enabled.html)

### ssm-document-not-public

>アカウントが所有する AWS Systems Manager ドキュメントがパブリックであるかどうかを確認します。所有者が「Self」になっている SSM ドキュメントがパブリックである場合、このルールは NON_COMPLIANT です。
>[ssm-document-not-public](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/ssm-document-not-public.html)

### subnet-auto-assign-public-ip-disabled

>Amazon Virtual Private Cloud (Amazon VPC) サブネットにパブリック IP アドレスが割り当てられているかどうかを確認します。Amazon VPC にパブリック IP アドレスが割り当てられているサブネットがない場合、ルールは COMPLIANT です。Amazon VPC にパブリック IP アドレスが割り当てられているサブネットがある場合、ルールは NON_COMPLIANT です。
>[subnet-auto-assign-public-ip-disabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/subnet-auto-assign-public-ip-disabled.html)

### virtualmachine-resources-protected-by-backup-plan

>AWS Backup-Gateway VirtualMachines が、バックアップ計画で保護されているかどうかをチェックします。Backup-Gateway VirtualMachine がバックアップ計画の対象でない場合、ルールは NON_COMPLIANT です。
>[virtualmachine-resources-protected-by-backup-plan](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/virtualmachine-resources-protected-by-backup-plan.html)

### vpc-default-security-group-closed

>Amazon Virtual Private Cloud (VPC) のデフォルトのセキュリティグループで、インバウンドとアウトバウンドのいずれのトラフィックも許可されていないことを確認します。セキュリティグループがデフォルトでない場合、ルールは NOT_APPLICABLE を返します。デフォルトのセキュリティグループに 1 つ以上のインバウンドトラフィックまたはアウトバウンドトラフィックがある場合、ルールは NON_COMPLIANT です。
>[vpc-default-security-group-closed](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/vpc-default-security-group-closed.html)

### vpc-flow-logs-enabled

>Amazon Virtual Private Cloud フローログが見つかったかどうか、および Amazon VPC に対して有効になっているかどうかを確認します。
>[vpc-flow-logs-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/vpc-flow-logs-enabled.html)

### vpc-network-acl-unused-check

>未使用のネットワークアクセスコントロールリスト (ネットワーク ACL) があるかどうかを確認します。各ネットワーク ACL がサブネットに関連付けられている場合、ルールは COMPLIANT です。ネットワーク ACL がサブネットに関連付けられていない場合、ルールは NON_COMPLIANT です。
>[vpc-network-acl-unused-check](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/vpc-network-acl-unused-check.html)

### vpc-sg-open-only-to-authorized-ports

>インバウンド 0.0.0.0/0 のセキュリティグループに TCP または UDP ポートでアクセス可能かどうかを確認します。インバウンド 0.0.0.0/0 のセキュリティグループにアクセス可能なポートがあり、これがルールパラメータで指定されていない場合、ルールは NON_COMPLIANT です。
>[vpc-sg-open-only-to-authorized-ports](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/vpc-sg-open-only-to-authorized-ports.html)

### vpc-vpn-2-tunnels-up

>AWS Site-to-Site VPN が提供する両方の VPN トンネルが UP ステータスであることを確認します。1 つまたは両方のトンネルのステータスが DOWN の場合、ルールは NON_COMPLIANT を返します。
>[vpc-vpn-2-tunnels-up](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/vpc-vpn-2-tunnels-up.html)

### wafv2-logging-enabled

>AWS ウェブアプリケーションファイアウォール (WAFV2) のリージョンおよびグローバルウェブアクセスコントロールリスト (ACL) でログ記録が有効になっているかどうかを確認します。ログ記録が有効になっていても、ログ記録の送信先がパラメータの値と一致しない場合、ルールは NON_COMPLIANT です。
>[wafv2-logging-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/wafv2-logging-enabled.html)

### waf-classic-logging-enabled

>AWS ウェブアプリケーションファイアウォール (WAF) の従来のグローバルウェブ ACL でログ記録が有効になっているかどうかを確認します。ログ記録が有効になっていない場合、このルールはグローバルウェブ ACL に対して NON_COMPLIANT です。
>[waf-classic-logging-enabled](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/waf-classic-logging-enabled.html)

### waf-global-rulegroup-not-empty

>AWS WAF Classic ルールグループに任意のルールが含まれているかどうかをチェックします。ルールグループにルールがない場合、ルールは NON_COMPLIANT になります。
>[waf-global-rulegroup-not-empty](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/waf-global-rulegroup-not-empty.html)

### waf-global-rule-not-empty

>AWS WAF グローバルルールに任意の条件が含まれているかどうかをチェックします。WAF グローバルルール内に条件がない場合、ルールは NON_COMPLIANT です。
>[waf-global-rule-not-empty](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/waf-global-rule-not-empty.html)

### waf-global-webacl-not-empty

>WAF のグローバルウェブ ACL に WAF ルールまたはルールグループが含まれているかどうかを確認します。ウェブ ACL に WAF ルールまたはルールグループが含まれていない場合、ルールは NON_COMPLIANT になります。
>[waf-global-webacl-not-empty](https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/waf-global-webacl-not-empty.html)

