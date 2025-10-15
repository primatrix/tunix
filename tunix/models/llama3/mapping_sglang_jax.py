"""Mappings for converting Llama3 weights to the Sglang-jax JAX backend."""

from __future__ import annotations

import os
from typing import Any, Dict, Tuple

Sharding = Tuple[str | None, ...]
MappingEntry = Tuple[str, Sharding]


def _to_sglang_jax_mappings() -> Dict[str, MappingEntry]:
  return {
      'lm_head.w': ('lm_head.embedding', (None, 'model')),
      'embedder.input_embedding': (
          'transformer.embed_tokens.embedding',
          ('model', None),
      ),
      'layers.*.input_layernorm.w': (
          'transformer.layers.*.input_layernorm.scale',
          (None,),
      ),
      'layers.*.mlp.down_proj.kernel': (
          'transformer.layers.*.mlp.down_proj.weight',
          ('model', None),
      ),
      'layers.*.mlp.gate_proj.kernel': (
          'transformer.layers.*.mlp.gate_proj.weight',
          (None, 'model'),
      ),
      'layers.*.mlp.up_proj.kernel': (
          'transformer.layers.*.mlp.up_proj.weight',
          (None, 'model'),
      ),
      'layers.*.post_attention_layernorm.w': (
          'transformer.layers.*.post_attention_layernorm.scale',
          (None,),
      ),
      'layers.*.attn.k_proj.w': (
          'transformer.layers.*.self_attn.k_proj.weight',
          (None, 'model', None),
      ),
      'layers.*.attn.o_proj.w': (
          'transformer.layers.*.self_attn.o_proj.weight',
          ('model', None, None),
      ),
      'layers.*.attn.q_proj.w': (
          'transformer.layers.*.self_attn.q_proj.weight',
          (None, 'model', None),
      ),
      'layers.*.attn.v_proj.w': (
          'transformer.layers.*.self_attn.v_proj.weight',
          (None, 'model', None),
      ),
      'final_norm.w': ('transformer.norm.scale', (None,)),
  }


def _lora_to_sglang_jax_mappings() -> Dict[str, MappingEntry] | None:
  """The lora parameter key mapping between Tunix vanilla model and Sglang-jax Jax backend"""
  return None


def _to_sglang_jax_transpose_keys():
  return {
      'lm_head.w': (1, 0),
  }


def _to_sglang_jax_hook_fns() -> Dict[str, Any] | None:
  """Additional parameter manipulation hook between Tunix vanilla model and Sglang Jax backend"""
  return None


SGLANG_JAX_MAPPING: Dict[str, Any] = {
    'to_hf_mappings': _to_sglang_jax_mappings(),
    'lora_to_hf_mappings': _lora_to_sglang_jax_mappings(),
    'to_hf_transpose_keys': _to_sglang_jax_transpose_keys(),
    'to_hf_hook_fns': _to_sglang_jax_hook_fns(),
}

__all__ = [
    'SGLANG_JAX_MAPPING',
]
