#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tbb
Version  : 2017_20161128oss_src
Release  : 17
URL      : https://www.threadingbuildingblocks.org/sites/default/files/software_releases/source/tbb2017_20161128oss_src.tgz
Source0  : https://www.threadingbuildingblocks.org/sites/default/files/software_releases/source/tbb2017_20161128oss_src.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: tbb-lib
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: build.patch
Patch2: timestamp.patch

%description
See index.html for directions and documentation.
If source is present (./Makefile and src/ directories),
type 'gmake' in this directory to build and test.

%package dev
Summary: dev components for the tbb package.
Group: Development
Requires: tbb-lib
Provides: tbb-devel

%description dev
dev components for the tbb package.


%package lib
Summary: lib components for the tbb package.
Group: Libraries

%description lib
lib components for the tbb package.


%prep
%setup -q -n tbb2017_20161128oss
%patch1 -p1
%patch2 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484453146
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1484453146
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/serial/tbb/parallel_for.h
/usr/include/serial/tbb/tbb_annotate.h
/usr/include/tbb/aggregator.h
/usr/include/tbb/aligned_space.h
/usr/include/tbb/atomic.h
/usr/include/tbb/blocked_range.h
/usr/include/tbb/blocked_range2d.h
/usr/include/tbb/blocked_range3d.h
/usr/include/tbb/cache_aligned_allocator.h
/usr/include/tbb/combinable.h
/usr/include/tbb/compat/condition_variable
/usr/include/tbb/compat/ppl.h
/usr/include/tbb/compat/thread
/usr/include/tbb/compat/tuple
/usr/include/tbb/concurrent_hash_map.h
/usr/include/tbb/concurrent_lru_cache.h
/usr/include/tbb/concurrent_priority_queue.h
/usr/include/tbb/concurrent_queue.h
/usr/include/tbb/concurrent_unordered_map.h
/usr/include/tbb/concurrent_unordered_set.h
/usr/include/tbb/concurrent_vector.h
/usr/include/tbb/critical_section.h
/usr/include/tbb/enumerable_thread_specific.h
/usr/include/tbb/flow_graph.h
/usr/include/tbb/flow_graph_abstractions.h
/usr/include/tbb/flow_graph_opencl_node.h
/usr/include/tbb/gfx_factory.h
/usr/include/tbb/global_control.h
/usr/include/tbb/index.html
/usr/include/tbb/internal/_aggregator_impl.h
/usr/include/tbb/internal/_concurrent_queue_impl.h
/usr/include/tbb/internal/_concurrent_unordered_impl.h
/usr/include/tbb/internal/_flow_graph_async_msg_impl.h
/usr/include/tbb/internal/_flow_graph_impl.h
/usr/include/tbb/internal/_flow_graph_indexer_impl.h
/usr/include/tbb/internal/_flow_graph_item_buffer_impl.h
/usr/include/tbb/internal/_flow_graph_join_impl.h
/usr/include/tbb/internal/_flow_graph_node_impl.h
/usr/include/tbb/internal/_flow_graph_streaming_node.h
/usr/include/tbb/internal/_flow_graph_tagged_buffer_impl.h
/usr/include/tbb/internal/_flow_graph_trace_impl.h
/usr/include/tbb/internal/_flow_graph_types_impl.h
/usr/include/tbb/internal/_mutex_padding.h
/usr/include/tbb/internal/_range_iterator.h
/usr/include/tbb/internal/_tbb_hash_compare_impl.h
/usr/include/tbb/internal/_tbb_strings.h
/usr/include/tbb/internal/_tbb_windef.h
/usr/include/tbb/internal/_template_helpers.h
/usr/include/tbb/internal/_x86_eliding_mutex_impl.h
/usr/include/tbb/internal/_x86_rtm_rw_mutex_impl.h
/usr/include/tbb/machine/gcc_armv7.h
/usr/include/tbb/machine/gcc_generic.h
/usr/include/tbb/machine/gcc_ia32_common.h
/usr/include/tbb/machine/gcc_itsx.h
/usr/include/tbb/machine/ibm_aix51.h
/usr/include/tbb/machine/icc_generic.h
/usr/include/tbb/machine/linux_common.h
/usr/include/tbb/machine/linux_ia32.h
/usr/include/tbb/machine/linux_ia64.h
/usr/include/tbb/machine/linux_intel64.h
/usr/include/tbb/machine/mac_ppc.h
/usr/include/tbb/machine/macos_common.h
/usr/include/tbb/machine/mic_common.h
/usr/include/tbb/machine/msvc_armv7.h
/usr/include/tbb/machine/msvc_ia32_common.h
/usr/include/tbb/machine/sunos_sparc.h
/usr/include/tbb/machine/windows_api.h
/usr/include/tbb/machine/windows_ia32.h
/usr/include/tbb/machine/windows_intel64.h
/usr/include/tbb/memory_pool.h
/usr/include/tbb/mutex.h
/usr/include/tbb/null_mutex.h
/usr/include/tbb/null_rw_mutex.h
/usr/include/tbb/parallel_do.h
/usr/include/tbb/parallel_for.h
/usr/include/tbb/parallel_for_each.h
/usr/include/tbb/parallel_invoke.h
/usr/include/tbb/parallel_reduce.h
/usr/include/tbb/parallel_scan.h
/usr/include/tbb/parallel_sort.h
/usr/include/tbb/parallel_while.h
/usr/include/tbb/partitioner.h
/usr/include/tbb/pipeline.h
/usr/include/tbb/queuing_mutex.h
/usr/include/tbb/queuing_rw_mutex.h
/usr/include/tbb/reader_writer_lock.h
/usr/include/tbb/recursive_mutex.h
/usr/include/tbb/runtime_loader.h
/usr/include/tbb/scalable_allocator.h
/usr/include/tbb/spin_mutex.h
/usr/include/tbb/spin_rw_mutex.h
/usr/include/tbb/task.h
/usr/include/tbb/task_arena.h
/usr/include/tbb/task_group.h
/usr/include/tbb/task_scheduler_init.h
/usr/include/tbb/task_scheduler_observer.h
/usr/include/tbb/tbb.h
/usr/include/tbb/tbb_allocator.h
/usr/include/tbb/tbb_config.h
/usr/include/tbb/tbb_exception.h
/usr/include/tbb/tbb_machine.h
/usr/include/tbb/tbb_profiling.h
/usr/include/tbb/tbb_stddef.h
/usr/include/tbb/tbb_thread.h
/usr/include/tbb/tbbmalloc_proxy.h
/usr/include/tbb/tick_count.h
/usr/lib64/libtbb.so
/usr/lib64/libtbbmalloc.so
/usr/lib64/libtbbmalloc_proxy.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtbb.so.2
/usr/lib64/libtbbmalloc.so.2
/usr/lib64/libtbbmalloc_proxy.so.2
