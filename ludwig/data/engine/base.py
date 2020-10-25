#! /usr/bin/env python
# coding=utf-8
# Copyright (c) 2020 Uber Technologies, Inc.
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
# ==============================================================================

from abc import ABC, abstractmethod


class DataProcessingEngine(ABC):
    @abstractmethod
    def parallelize(self, data):
        raise NotImplementedError()

    @abstractmethod
    def persist(self, data):
        raise NotImplementedError()

    @abstractmethod
    def compute(self, data):
        raise NotImplementedError()

    @abstractmethod
    def array_to_col(self, array):
        raise NotImplementedError()

    @abstractmethod
    def create_dataset(self, dataset, tag, config, training_set_metadata):
        raise NotImplementedError()

    @property
    @abstractmethod
    def dtypes(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def array_lib(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def df_lib(self):
        raise NotImplementedError()

    @property
    @abstractmethod
    def use_hdf5_cache(self):
        raise NotImplementedError()