#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tbb
Version  : 2021.5.0
Release  : 33
URL      : https://github.com/01org/tbb/archive/v2021.5.0/tbb-2021.5.0.tar.gz
Source0  : https://github.com/01org/tbb/archive/v2021.5.0/tbb-2021.5.0.tar.gz
Summary  : C++ library for parallel programming on multi-core processors.
Group    : Development/Tools
License  : Apache-2.0
Requires: tbb-lib = %{version}-%{release}
Requires: tbb-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : pkg-config
BuildRequires : python3

%description
# oneAPI Threading Building Blocks
[![Apache License Version 2.0](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE.txt) [![oneTBB CI](https://github.com/oneapi-src/oneTBB/actions/workflows/ci.yml/badge.svg)](https://github.com/oneapi-src/oneTBB/actions/workflows/ci.yml?query=branch%3Amaster)

%package dev
Summary: dev components for the tbb package.
Group: Development
Requires: tbb-lib = %{version}-%{release}
Provides: tbb-devel = %{version}-%{release}
Requires: tbb = %{version}-%{release}

%description dev
dev components for the tbb package.


%package doc
Summary: doc components for the tbb package.
Group: Documentation

%description doc
doc components for the tbb package.


%package lib
Summary: lib components for the tbb package.
Group: Libraries
Requires: tbb-license = %{version}-%{release}
Requires: compat-tbb-soname2-lib

%description lib
lib components for the tbb package.


%package license
Summary: license components for the tbb package.
Group: Default

%description license
license components for the tbb package.


%prep
%setup -q -n oneTBB-2021.5.0
cd %{_builddir}/oneTBB-2021.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640290001
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%cmake ..
make  %{?_smp_mflags}  DEFAULTFLAGS="$CFLAGS"
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1640290001
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tbb
cp %{_builddir}/oneTBB-2021.5.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/tbb/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/oneapi/tbb.h
/usr/include/oneapi/tbb/blocked_range.h
/usr/include/oneapi/tbb/blocked_range2d.h
/usr/include/oneapi/tbb/blocked_range3d.h
/usr/include/oneapi/tbb/blocked_rangeNd.h
/usr/include/oneapi/tbb/cache_aligned_allocator.h
/usr/include/oneapi/tbb/collaborative_call_once.h
/usr/include/oneapi/tbb/combinable.h
/usr/include/oneapi/tbb/concurrent_hash_map.h
/usr/include/oneapi/tbb/concurrent_lru_cache.h
/usr/include/oneapi/tbb/concurrent_map.h
/usr/include/oneapi/tbb/concurrent_priority_queue.h
/usr/include/oneapi/tbb/concurrent_queue.h
/usr/include/oneapi/tbb/concurrent_set.h
/usr/include/oneapi/tbb/concurrent_unordered_map.h
/usr/include/oneapi/tbb/concurrent_unordered_set.h
/usr/include/oneapi/tbb/concurrent_vector.h
/usr/include/oneapi/tbb/detail/_aggregator.h
/usr/include/oneapi/tbb/detail/_aligned_space.h
/usr/include/oneapi/tbb/detail/_allocator_traits.h
/usr/include/oneapi/tbb/detail/_assert.h
/usr/include/oneapi/tbb/detail/_concurrent_queue_base.h
/usr/include/oneapi/tbb/detail/_concurrent_skip_list.h
/usr/include/oneapi/tbb/detail/_concurrent_unordered_base.h
/usr/include/oneapi/tbb/detail/_config.h
/usr/include/oneapi/tbb/detail/_containers_helpers.h
/usr/include/oneapi/tbb/detail/_exception.h
/usr/include/oneapi/tbb/detail/_export.h
/usr/include/oneapi/tbb/detail/_flow_graph_body_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_cache_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_indexer_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_item_buffer_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_join_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_node_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_node_set_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_nodes_deduction.h
/usr/include/oneapi/tbb/detail/_flow_graph_tagged_buffer_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_trace_impl.h
/usr/include/oneapi/tbb/detail/_flow_graph_types_impl.h
/usr/include/oneapi/tbb/detail/_hash_compare.h
/usr/include/oneapi/tbb/detail/_intrusive_list_node.h
/usr/include/oneapi/tbb/detail/_machine.h
/usr/include/oneapi/tbb/detail/_mutex_common.h
/usr/include/oneapi/tbb/detail/_namespace_injection.h
/usr/include/oneapi/tbb/detail/_node_handle.h
/usr/include/oneapi/tbb/detail/_pipeline_filters.h
/usr/include/oneapi/tbb/detail/_pipeline_filters_deduction.h
/usr/include/oneapi/tbb/detail/_range_common.h
/usr/include/oneapi/tbb/detail/_rtm_mutex.h
/usr/include/oneapi/tbb/detail/_rtm_rw_mutex.h
/usr/include/oneapi/tbb/detail/_scoped_lock.h
/usr/include/oneapi/tbb/detail/_segment_table.h
/usr/include/oneapi/tbb/detail/_small_object_pool.h
/usr/include/oneapi/tbb/detail/_string_resource.h
/usr/include/oneapi/tbb/detail/_task.h
/usr/include/oneapi/tbb/detail/_task_handle.h
/usr/include/oneapi/tbb/detail/_template_helpers.h
/usr/include/oneapi/tbb/detail/_utils.h
/usr/include/oneapi/tbb/detail/_waitable_atomic.h
/usr/include/oneapi/tbb/enumerable_thread_specific.h
/usr/include/oneapi/tbb/flow_graph.h
/usr/include/oneapi/tbb/flow_graph_abstractions.h
/usr/include/oneapi/tbb/global_control.h
/usr/include/oneapi/tbb/info.h
/usr/include/oneapi/tbb/memory_pool.h
/usr/include/oneapi/tbb/mutex.h
/usr/include/oneapi/tbb/null_mutex.h
/usr/include/oneapi/tbb/null_rw_mutex.h
/usr/include/oneapi/tbb/parallel_for.h
/usr/include/oneapi/tbb/parallel_for_each.h
/usr/include/oneapi/tbb/parallel_invoke.h
/usr/include/oneapi/tbb/parallel_pipeline.h
/usr/include/oneapi/tbb/parallel_reduce.h
/usr/include/oneapi/tbb/parallel_scan.h
/usr/include/oneapi/tbb/parallel_sort.h
/usr/include/oneapi/tbb/partitioner.h
/usr/include/oneapi/tbb/profiling.h
/usr/include/oneapi/tbb/queuing_mutex.h
/usr/include/oneapi/tbb/queuing_rw_mutex.h
/usr/include/oneapi/tbb/rw_mutex.h
/usr/include/oneapi/tbb/scalable_allocator.h
/usr/include/oneapi/tbb/spin_mutex.h
/usr/include/oneapi/tbb/spin_rw_mutex.h
/usr/include/oneapi/tbb/task.h
/usr/include/oneapi/tbb/task_arena.h
/usr/include/oneapi/tbb/task_group.h
/usr/include/oneapi/tbb/task_scheduler_observer.h
/usr/include/oneapi/tbb/tbb_allocator.h
/usr/include/oneapi/tbb/tbbmalloc_proxy.h
/usr/include/oneapi/tbb/tick_count.h
/usr/include/oneapi/tbb/version.h
/usr/include/tbb/blocked_range.h
/usr/include/tbb/blocked_range2d.h
/usr/include/tbb/blocked_range3d.h
/usr/include/tbb/blocked_rangeNd.h
/usr/include/tbb/cache_aligned_allocator.h
/usr/include/tbb/collaborative_call_once.h
/usr/include/tbb/combinable.h
/usr/include/tbb/concurrent_hash_map.h
/usr/include/tbb/concurrent_lru_cache.h
/usr/include/tbb/concurrent_map.h
/usr/include/tbb/concurrent_priority_queue.h
/usr/include/tbb/concurrent_queue.h
/usr/include/tbb/concurrent_set.h
/usr/include/tbb/concurrent_unordered_map.h
/usr/include/tbb/concurrent_unordered_set.h
/usr/include/tbb/concurrent_vector.h
/usr/include/tbb/enumerable_thread_specific.h
/usr/include/tbb/flow_graph.h
/usr/include/tbb/flow_graph_abstractions.h
/usr/include/tbb/global_control.h
/usr/include/tbb/info.h
/usr/include/tbb/memory_pool.h
/usr/include/tbb/null_mutex.h
/usr/include/tbb/null_rw_mutex.h
/usr/include/tbb/parallel_for.h
/usr/include/tbb/parallel_for_each.h
/usr/include/tbb/parallel_invoke.h
/usr/include/tbb/parallel_pipeline.h
/usr/include/tbb/parallel_reduce.h
/usr/include/tbb/parallel_scan.h
/usr/include/tbb/parallel_sort.h
/usr/include/tbb/partitioner.h
/usr/include/tbb/profiling.h
/usr/include/tbb/queuing_mutex.h
/usr/include/tbb/queuing_rw_mutex.h
/usr/include/tbb/scalable_allocator.h
/usr/include/tbb/spin_mutex.h
/usr/include/tbb/spin_rw_mutex.h
/usr/include/tbb/task.h
/usr/include/tbb/task_arena.h
/usr/include/tbb/task_group.h
/usr/include/tbb/task_scheduler_observer.h
/usr/include/tbb/tbb.h
/usr/include/tbb/tbb_allocator.h
/usr/include/tbb/tbbmalloc_proxy.h
/usr/include/tbb/tick_count.h
/usr/include/tbb/version.h
/usr/lib64/cmake/TBB/TBBConfig.cmake
/usr/lib64/cmake/TBB/TBBConfigVersion.cmake
/usr/lib64/cmake/TBB/TBBTargets-relwithdebinfo.cmake
/usr/lib64/cmake/TBB/TBBTargets.cmake
/usr/lib64/libtbb.so
/usr/lib64/libtbbmalloc.so
/usr/lib64/libtbbmalloc_proxy.so
/usr/lib64/pkgconfig/tbb.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/TBB/README.md

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtbb.so.12
/usr/lib64/libtbb.so.12.5
/usr/lib64/libtbbmalloc.so.2
/usr/lib64/libtbbmalloc.so.2.5
/usr/lib64/libtbbmalloc_proxy.so.2
/usr/lib64/libtbbmalloc_proxy.so.2.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tbb/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
