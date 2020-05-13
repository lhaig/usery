workflow "automerge pull requests on updates" {
  on = "pull_request"
  resolves = ["automerge"]
}

action "automerge" {
  uses = "pascalgn/automerge-action@9d655352861c757731df72b6ac21d65fdf6d92ee"
  secrets = ["GITHUB_TOKEN"]
  MERGE_REMOVE_LABELS: "automerge"
  MERGE_METHOD: "squash"
  MERGE_COMMIT_MESSAGE: "pull-request-title-and-description"
  MERGE_FORKS: "false"
  MERGE_DELETE_BRANCH: "true"
}
