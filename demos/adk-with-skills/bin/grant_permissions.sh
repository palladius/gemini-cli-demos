#!/bin/bash
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This script helps to grant the necessary permissions for deploying to Agent Engine (GEAP).
# It grants the 'AI Platform Reasoning Engine Creator' role to the current active account.

set -e

PROJECT_ID="palladius-genai"
ACCOUNT=$(gcloud config get-value account)

echo "Granting roles/aiplatform.admin to $ACCOUNT on project $PROJECT_ID..."

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="user:$ACCOUNT" \
    --role="roles/aiplatform.admin"

echo "Done. You may need to wait a few minutes for IAM changes to propagate before running 'just deploy'."
