#!/usr/bin/env bash
# setup-doctor: read-only Mac environment check.
# Does NOT install or modify anything.
set -euo pipefail

TOOL="all"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool)
      TOOL="${2:-all}"
      shift 2
      ;;
    -h|--help)
      cat <<'EOF'
Usage: bash scripts/doctor.sh [--tool all|claude-code|codex|deepseek-harness|hyperframes|claude-desktop]

Read-only checks for Mac. Prints plain-language pass/fail lines.
Node version rules differ by tool — reports name the tool requirement.
EOF
      exit 0
      ;;
    *)
      echo "Unknown arg: $1" >&2
      exit 2
      ;;
  esac
done

os_name="$(uname -s || true)"
if [[ "$os_name" != "Darwin" ]]; then
  echo "【系统】没通过：当前是 ${os_name:-unknown}。本 skill 第一版只支持 Mac（Darwin）。"
  echo "提示：仍会继续打印通用命令检查，但修复步骤以 Mac 为准。"
fi

have_cmd() { command -v "$1" >/dev/null 2>&1; }

version_ge() {
  # semver-ish: return 0 if $1 >= $2
  local IFS=.
  local i a=($1) b=($2)
  for ((i = 0; i < 3; i++)); do
    local ai="${a[i]:-0}" bi="${b[i]:-0}"
    ai="${ai//[^0-9]/}"
    bi="${bi//[^0-9]/}"
    ai="${ai:-0}"
    bi="${bi:-0}"
    if ((10#$ai > 10#$bi)); then return 0; fi
    if ((10#$ai < 10#$bi)); then return 1; fi
  done
  return 0
}

echo "=== setup-doctor 自检（只读）==="
echo "工具范围: ${TOOL}"
echo

# --- git ---
if have_cmd git; then
  echo "【git】通过：$(git --version 2>/dev/null | head -1)"
else
  echo "【git】没通过：未找到 git。许多 CLI 安装与 skill 仓库克隆需要 git。"
fi

# --- python ---
if have_cmd python3; then
  echo "【Python】通过：$(python3 --version 2>/dev/null | head -1)"
else
  echo "【Python】没通过：未找到 python3（部分工具链或脚本会用到）。"
fi

# --- node base ---
NODE_VER=""
if have_cmd node; then
  NODE_VER="$(node --version 2>/dev/null | sed 's/^v//')"
  echo "【Node】已安装：v${NODE_VER}"
else
  echo "【Node】没通过：未找到 node。若你要装的工具依赖 Node，请先安装 Node。"
fi

check_node_for() {
  local label="$1"
  local need="$2"
  local doc="$3"
  if [[ -z "$NODE_VER" ]]; then
    echo "【Node · ${label}】没通过：需要 Node ${need}+（${label} 的要求）。说明：${doc}"
    return
  fi
  if version_ge "$NODE_VER" "$need"; then
    echo "【Node · ${label}】通过：当前 v${NODE_VER}，满足 ${label} 要求的 ${need}+。出处：${doc}"
  else
    echo "【Node · ${label}】没通过：当前 v${NODE_VER}，但 ${label} 要求 Node ${need}+。出处：${doc}"
  fi
}

# Per-tool Node requirements (review round 2):
# - Claude Code via npm: 22+
# - HyperFrames: 22+
# - DeepSeek Harness: per official docs (currently 24.9+)
need_claude=false
need_hf=false
need_dsh=false
case "$TOOL" in
  all)
    need_claude=true; need_hf=true; need_dsh=true
    ;;
  claude-code) need_claude=true ;;
  hyperframes) need_hf=true ;;
  deepseek-harness) need_dsh=true ;;
  codex|claude-desktop) ;;
  *)
    echo "未知 --tool: $TOOL（将跳过分工具 Node 判断）" >&2
    ;;
esac

if $need_claude; then
  check_node_for "Claude Code（npm 安装）" "22.0.0" \
    "https://code.claude.com/docs/en/setup"
fi
if $need_hf; then
  check_node_for "HyperFrames" "22.0.0" \
    "https://github.com/heygen-com/hyperframes"
fi
if $need_dsh; then
  # Official upgrade guide currently states Node.js 24.9+; re-check docs if this drifts.
  check_node_for "DeepSeek Harness" "24.9.0" \
    "https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/upgrade-guide/v0.2.1-rc.2/node-24/guide.md"
fi

# --- CLI presence (informational) ---
for pair in "claude:Claude Code" "codex:Codex" "ffmpeg:ffmpeg"; do
  cmd="${pair%%:*}"
  label="${pair##*:}"
  if have_cmd "$cmd"; then
    echo "【命令 · ${label}】通过：找到 \`${cmd}\`"
  else
    echo "【命令 · ${label}】未找到 \`${cmd}\`（若你不装该工具可忽略）"
  fi
done

# --- network: DNS/HTTP reachability to documentation hosts (read-only GET) ---
echo
echo "=== 网络连通（官方文档域名，失败只提示）==="
hosts=(
  "https://code.claude.com/docs/en/setup"
  "https://learn.chatgpt.com/docs/codex/cli"
  "https://claude.com/docs/skills/how-to"
  "https://github.com/deepseek-ai/deepseek-harness"
)
if have_cmd curl; then
  for url in "${hosts[@]}"; do
    code="$(curl -sS -o /dev/null -w '%{http_code}' --connect-timeout 5 --max-time 10 -L "$url" || true)"
    if [[ "$code" =~ ^[23] ]]; then
      echo "【网络】通过：${url} → HTTP ${code}"
    else
      echo "【网络】没通过/不稳：${url} → HTTP ${code:-error}（公司代理或地区网络可能导致；以官方说明为准）"
    fi
  done
else
  echo "【网络】跳过：未找到 curl"
fi

echo
echo "自检结束。匹配具体报错请打开 setup-doctor/errors/；库中没有就去仓库提 issue，不要猜测。"
